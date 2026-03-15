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

    main_menu = {
        "keyboard": [
            [{"text": "📅 Book a Court"}, {"text": "🎒 Junior Programs"}],
            [{"text": "🎾 Adult Lessons"}, {"text": "🥒 Pickleball Info"}],
            [{"text": "❓ Ask a Question"}, {"text": "📞 Request Call-back"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True
    }

    # 1. Direct Button Matches
    if user_text in ["/start", "Menu", "🏠 Start Again"]:
        response_text = "Welcome to Kim Warwick Tennis Academy! How can we help you get on court today?"
        markup = main_menu

    elif user_text == "📅 Book a Court":
        response_text = "Ready to play? You can view real-time availability and book your court here:"
        markup = {
            "inline_keyboard": [[{"text": "🌐 Open Booking Portal", "url": "https://www.kwta.com.au/book-a-court/"}]]
        }

    elif user_text == "🎒 Junior Programs":
        response_text = "We have programs for every stage! Are you looking for Hot Shots (ages 4-12) or our Elite Squads?"
        markup = {
            "inline_keyboard": [
                [{"text": "Under 12 (Hot Shots)", "callback_data": "js_hotshots"}],
                [{"text": "Teens / Elite Squads", "callback_data": "js_elite"}]
            ]
        }

    elif user_text == "🎾 Adult Lessons":
        response_text = "Improve your game with our adult sessions! We offer Group Classes, Cardio Tennis, and Ladies Clinicals."
        markup = {
            "inline_keyboard": [[{"text": "View Class Timetable", "url": "https://www.kwta.com.au/adult-programs/"}]]
        }

    elif user_text == "🥒 Pickleball Info":
        response_text = "Join the Pickleball craze! We have dedicated courts with social play Monday mornings and Friday nights."
        markup = {
            "inline_keyboard": [[{"text": "🥒 Pickleball Details", "url": "https://www.kwta.com.au/pickleball/"}]]
        }

    elif user_text == "📞 Request Call-back":
        response_text = "No problem. Please type your phone number and a preferred time below, and our team will be in touch!"
        markup = None # User needs to type now

    else:
        response_text = geminiClient.get_gemini_response(user_text) # Call LLM to handle response
        
        # When AI answers, we give them a one-time keyboard to continue or restart
        markup = {
            "keyboard": [
                [{"text": "❓ Ask another Question"}],
                [{"text": "📞 Request Call-back"}, {"text": "🏠 Start Again"}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": True
        }

    payload = {
        "chat_id": chat_id,
        "text": response_text,
        "reply_markup": markup,
        "parse_mode": "Markdown"
    }
    
    telegramClient.send_telegram_message(payload)
    return "OK", 200