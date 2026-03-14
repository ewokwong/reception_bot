from flask import Flask, request
import json
import logging
import os

from handlers import messageHandler, commandHandler, buttonHandler

app = Flask(__name__)

# Configure logging to output to the console (which shows up in Cloud Run logs)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['POST'])
def webhook():
    logging.info("Application startup complete")
    # 1. Get the JSON data from the request
    data = request.get_json(force=True)
    
    message = data.get('message', {})
    text = message.get('text', '')

    if text:
        if text.startswith('/'):
            return commandHandler.processMessage(data)
    elif 'callback_query' in data:  # Button clicks
        return buttonHandler.processMessage(data)
    else:
        return messageHandler.processMessage(data)
    
    # 4. Fallback for non-text messages (photos, voice, etc.)
    logging.info("Received a non-text update (e.g., photo or sticker)")
    return "OK", 200