from __future__ import annotations

import threading
import time
from collections import deque
from datetime import datetime
from pathlib import Path

import cv2
import serial
from serial import SerialException

from ai_models.model_loader import HumanDetector
from config import (
    ALERT_COOLDOWN_SECONDS,
    CAMERA_INDEX,
    DASHBOARD_HOST,
    DASHBOARD_PORT,
    SERIAL_BAUD,
    SERIAL_PORT,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
)
from telegram_notifier import send_telegram_message
from web_dashboard import create_app


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def append_event(state: dict, message: str) -> None:
    state["events"].appendleft(f"[{now()}] {message}")


def serial_worker(state: dict, stop_event: threading.Event) -> None:
    while not stop_event.is_set():
        try:
            with serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1) as ser:
                append_event(state, f"Serial connected on {SERIAL_PORT}")
                while not stop_event.is_set():
                    raw = ser.readline().decode(errors="ignore").strip()
                    if raw:
                        state["last_serial_event"] = raw
                        append_event(state, f"Serial: {raw}")
        except SerialException as exc:
            append_event(state, f"Serial error: {exc}")
            time.sleep(3)


def dashboard_worker(state: dict) -> None:
    app = create_app(state)
    app.run(host=DASHBOARD_HOST, port=DASHBOARD_PORT, debug=False, use_reloader=False)


def should_alert(state: dict, humans_detected: int) -> bool:
    if humans_detected <= 0:
        return False
    if state["last_serial_event"] != "MOTION_DETECTED":
        return False
    last_alert_ts = state.get("last_alert_ts", 0.0)
    return (time.time() - last_alert_ts) >= ALERT_COOLDOWN_SECONDS


def main() -> None:
    state = {
        "last_serial_event": "",
        "last_human_count": 0,
        "last_alert_time": "",
        "last_alert_ts": 0.0,
        "events": deque(maxlen=50),
    }

    stop_event = threading.Event()
    serial_thread = threading.Thread(target=serial_worker, args=(state, stop_event), daemon=True)
    web_thread = threading.Thread(target=dashboard_worker, args=(state,), daemon=True)

    serial_thread.start()
    web_thread.start()

    model_path = Path(__file__).resolve().parent / "ai_models" / "human_detector.pt"
    detector = HumanDetector(str(model_path) if model_path.exists() else None)

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        append_event(state, f"Camera open failed for index {CAMERA_INDEX}")
        print(f"Failed to open camera index {CAMERA_INDEX}")
        return

    append_event(state, "Full system started")
    print(f"Dashboard running on http://{DASHBOARD_HOST}:{DASHBOARD_PORT}")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                append_event(state, "Camera read failed")
                time.sleep(0.2)
                continue

            result = detector.detect(frame)
            human_count = len(result.humans)
            state["last_human_count"] = human_count

            if should_alert(state, human_count):
                msg = f"Alert: motion + human detected ({human_count})"
                sent = send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, msg)
                state["last_alert_ts"] = time.time()
                state["last_alert_time"] = now()
                append_event(state, f"Telegram {'sent' if sent else 'failed'}: {msg}")

            time.sleep(0.05)
    except KeyboardInterrupt:
        append_event(state, "Stopping system")
    finally:
        stop_event.set()
        cap.release()


if __name__ == "__main__":
    main()
