import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def startCommand(data):
    first_name = data['message']['from'].get('first_name', 'there')
    
    text = (
        f"Hello {first_name}! \n\n"
        "Welcome to **Kim Warwick Tennis Academy** digital assistant.\n\n"
        "What are you looking to do today? Select an option below:"
    )

    # Inline Buttons
    reply_markup = {
        "inline_keyboard": [
            [{"text": "📅 Book a Court", "callback_data": "book_court"}],
            [{"text": "🎒 Junior Programs", "callback_data": "junior_progs"}],
            [{"text": "🎾 Adult Lessons", "callback_data": "adult_lessons"}],
            [{"text": "🥒 Pickleball Info", "callback_data": "pickleball"}],
            [{"text": "📞 Speak to Staff", "callback_data": "contact_staff"}]
        ]
    }
    
    return text, reply_markup

def processMessage(data):
    # Check if it's a message or a button click (callback_query)
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
            
    # Handle the button clicks (This is how you 'probe' and respond)
    elif 'callback_query' in data:
        chat_id = data['callback_query']['message']['chat']['id']
        choice = data['callback_query']['data']
        
        # Define what happens when they click a button
        responses = {
            "book_court": "You can book courts at our Hornsby location via our portal: [Book Here](https://www.kwta.com.au/book-a-court/)",
            "junior_progs": "We offer Hot Shots (ages 4-12) and Elite Squads. Which age group are you inquiring for?",
            "pickleball": "We have dedicated Pickleball courts! Social play is available Monday mornings and Friday nights.",
            "contact_staff": "Our reception is open 9am-7pm. Call us at (02) 9477-6377."
        }
        
        payload = {
            "chat_id": chat_id,
            "text": responses.get(choice, "Options coming soon!"),
            "parse_mode": "Markdown"
        }

    requests.post(TELEGRAM_URL, json=payload)
    return "OK", 200