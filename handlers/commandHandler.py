import os

from clients import telegramClient

TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def startCommand(data):
    first_name = data['message']['from'].get('first_name', 'there')
    
    text = (
        f"Hello {first_name}! \n\n"
        "Welcome to KWTA's digital assistant.\n\n"
        "What are you looking to do today?"
    )

    reply_markup = {
        "keyboard": [
            [{"text": "📅 Book a Court"}],
            [{"text": "🎒 Junior Programs"}],
            [{"text": "🎾 Adult Lessons"}],
            [{"text": "🥒 Pickleball Info"}],
            [{"text": "📞 Something else"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True
    }
    
    return text, reply_markup

def processMessage(data):
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        incoming_text = data['message'].get('text', '')

        if incoming_text == '/start':
            response_text, markup = startCommand(data)
            payload = {
                "chat_id": chat_id,
                "text": response_text,
                "reply_markup": markup
            }

        else:
            payload = {
                "chat_id": chat_id,
                "text": "I didn't quite catch that. Try /start to see my options."
            }
            
        telegramClient.send_telegram_message(payload)
    return "OK", 200