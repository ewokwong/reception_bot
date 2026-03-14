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

    # Inline Buttons
    reply_markup = {
        "inline_keyboard": [
            [{"text": "📅 Book a Court", "callback_data": "book_court"}],
            [{"text": "🎒 Junior Programs", "callback_data": "junior_progs"}],
            [{"text": "🎾 Adult Lessons", "callback_data": "adult_lessons"}],
            [{"text": "🥒 Pickleball Info", "callback_data": "pickleball"}],
            [{"text": "📞 Something else", "callback_data": "something_else"}]
        ]
    }
    
    return text, reply_markup

def processMessage(data):
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            response_text, markup = startCommand(data)
            payload = {
                "chat_id": chat_id,
                "text": response_text,
                "reply_markup": markup,
                "parse_mode": "Markdown"
            }
        else:
            payload = {
                "chat_id": chat_id,
                "text": "That command is not available yet. Please type /start instead."
            }
            
    telegramClient.send_telegram_message(payload)
    return "OK", 200