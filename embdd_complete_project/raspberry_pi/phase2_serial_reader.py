from __future__ import annotations

import time

import serial

from config import SERIAL_BAUD, SERIAL_PORT


def main() -> None:
    print(f"Opening serial: {SERIAL_PORT} @ {SERIAL_BAUD}")
    while True:
        try:
            with serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1) as ser:
                print("Serial connected. Waiting for events...")
                while True:
                    raw = ser.readline().decode(errors="ignore").strip()
                    if raw:
                        print(raw)
        except serial.SerialException as exc:
            print(f"Serial error: {exc}. Retrying in 3s...")
            time.sleep(3)


if __name__ == "__main__":
    main()
