from __future__ import annotations

import requests


def send_telegram_message(bot_token: str, chat_id: str, text: str, timeout: int = 8) -> bool:
    if not bot_token or not chat_id:
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        resp = requests.post(url, json=payload, timeout=timeout)
        return resp.status_code == 200
    except requests.RequestException:
        return False
