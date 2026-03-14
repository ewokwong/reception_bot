from clients import geminiClient
from clients import telegramClient

def processMessage(data):
    message = data.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    user_text = message.get('text', '')

    if not chat_id or not user_text:
        return "OK", 200

    response_text = geminiClient.call_gemini(user_text)

    markup = {
        "inline_keyboard": [
            [{"text": "📞 Request a Call-back", "callback_data": "get_call"}]
        ]
    }

    payload = {
        "chat_id": chat_id,
        "text": response_text,
        "reply_markup": markup,
        "parse_mode": "Markdown"
    }
    
    telegramClient.send_telegram_message(payload)

    return "OK", 200