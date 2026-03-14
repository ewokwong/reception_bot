import requests
import os

from clients import telegramClient

def processMessage(data):
    chat_id = data['callback_query']['message']['chat']['id']
    choice = data['callback_query']['data']
    
    markup_list = []

    # Only add the 'Something Else' button if they aren't already on that screen
    if choice != "something_else":
        markup_list.append([{"text": "❓ Something else / Ask a question", "callback_data": "something_else"}])
        markup_list.append[{"text": "📞 Request a Call-back", "callback_data": "get_call"}]

    elif choice == "get_call":
        text = (
            "✅ **Request Received!**\n\n"
            "A member of our staff will call you soon at the number associated with your account.\n\n"
            "We appreciate your patience!"
        )
    
    elif choice == "book_court":
        text = "You can find pricing and book courts via our online portal below:"
        markup_list.append([{"text": "🌐 Open Booking Portal", "url": "https://www.kwta.com.au/book-a-court/"}])

    elif choice == "junior_progs":
        text = "We offer Hot Shots (ages 4-12) and Elite Squads. Which age group are you inquiring for?"
        markup_list.append([{"text": "Under 12 (Hot Shots)", "callback_data": "js_hotshots"}])
        markup_list.append([{"text": "Teens / Elite Squads", "callback_data": "js_elite"}])

    elif choice == "adult_lessons":
        text = (
            "We have programs for all levels! 🎾\n\n"
            "• **Group Classes:** Beginner to Intermediate\n"
            "• **Cardio Tennis:** High-energy fitness\n"
            "• **Ladies Clinicals:** Mid-week mornings\n"
            "• **Private:** 1-on-1 coaching"
        )
        markup_list.append([{"text": "View Class Timetable", "url": "https://www.kwta.com.au/adult-programs/"}])
        markup_list.append([{"text": "Inquire about Privates", "callback_data": "get_call"}])

    elif choice == "pickleball":
        text = "We have dedicated Pickleball courts! Social play is available Monday mornings and Friday nights."
        markup_list.append([{"text": "🥒 Pickleball Details", "url": "https://www.kwta.com.au/pickleball/"}])

    elif choice == "something_else":
        text = (
            "No problem! Please type your question below:"
        )

    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {"inline_keyboard": markup_list},
        "parse_mode": "Markdown"
    }
    
    telegramClient.send_telegram_message(payload)
    return "OK", 200