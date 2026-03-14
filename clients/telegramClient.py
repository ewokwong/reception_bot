import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_telegram_message(payload):
    requests.post(TELEGRAM_URL, json=payload)