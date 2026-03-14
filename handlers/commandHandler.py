import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def processMessage(data):
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    # 2. Command Logic
    if text == '/start':
        response_text = "Hello World!"
    else:
        response_text = "Command not yet implemented."

    # 3. Send the reply back to Telegram
    payload = {
        "chat_id": chat_id,
        "text": response_text
    }
    
    try:
        requests.post(TELEGRAM_URL, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

    return "OK", 200