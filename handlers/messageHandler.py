from clients import geminiClient
from clients import telegramClient

from clients import geminiClient
from clients import telegramClient

def processMessage(data):
    message = data.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    user_text = message.get('text', '')

    if not chat_id or not user_text:
        return "OK", 200

    response_text = ""
    markup = None # Default to no buttons

    # 2. Logic for Reply Keyboard Button Matches
    if user_text == "📅 Book a Court":
        response_text = "You can find pricing and book courts via our online portal below:"
        markup = {
            "inline_keyboard": [[{"text": "🌐 Open Booking Portal", "url": "https://www.kwta.com.au/book-a-court/"}]]
        }

    elif user_text == "🎒 Junior Programs":
        response_text = "We offer Hot Shots (ages 4-12) and Elite Squads. Which age group are you inquiring for?"
        markup = {
            "inline_keyboard": [
                [{"text": "Under 12 (Hot Shots)", "callback_data": "js_hotshots"}],
                [{"text": "Teens / Elite Squads", "callback_data": "js_elite"}]
            ]
        }

    elif user_text == "🎾 Adult Lessons":
        response_text = (
            "We have programs for all levels! 🎾\n\n"
            "• **Group Classes:** Beginner to Intermediate\n"
            "• **Cardio Tennis:** High-energy fitness\n"
            "• **Ladies Clinicals:** Mid-week mornings"
        )
        markup = {
            "inline_keyboard": [[{"text": "View Class Timetable", "url": "https://www.kwta.com.au/adult-programs/"}]]
        }

    elif user_text == "🥒 Pickleball Info":
        response_text = "We have dedicated Pickleball courts! Social play is available Monday mornings and Friday nights."
        markup = {
            "inline_keyboard": [[{"text": "🥒 Pickleball Details", "url": "https://www.kwta.com.au/pickleball/"}]]
        }

    elif user_text == "📞 Something else":
        response_text = "No problem! Please type your question below and I'll do my best to help."

    # 3. Fallback to Gemini if no button matches
    else:
        response_text = geminiClient.get_gemini_response(user_text)
        # Add a sticky "Request Call-back" button to AI responses
        markup = {
            "inline_keyboard": [[{"text": "📞 Request a Call-back", "callback_data": "get_call"}]]
        }

    # 4. Send the payload
    payload = {
        "chat_id": chat_id,
        "text": response_text,
        "reply_markup": markup,
        "parse_mode": "Markdown"
    }
    
    telegramClient.send_telegram_message(payload)
    return "OK", 200