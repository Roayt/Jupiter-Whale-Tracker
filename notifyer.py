"""Telegram notifier: sends whale alert messasges."""

import requests

from config import Telegram_bot_token,Telegram_chat_id

def send_telegram_alert(mnessage):
    url=f"https://api.telegram.org/bot{Telegram_bot_token}/sendMessage"
    payload={
        "chat_id":Telegram_chat_id,
        "text":mnessage,
        "parse_mode":"HTML",
    }

    try:
        response=requests.post(url,json=payload,timeout=10)
        print(f"Telegram Status:{response.status_code}")
        print(f"Telegram Response:{response.text}")
    except Exception as e:
        print(f"Telegram Alert Failed:{e}")

