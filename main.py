from flask import Flask, request
import json
import logging
import os

from handlers import messageHandler, commandHandler

app = Flask(__name__)

# Configure logging to output to the console (which shows up in Cloud Run logs)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['POST'])
def webhook():
    # 1. Get the JSON data from the request
    data = request.get_json(force=True)
    
    message = data.get('message', {})
    text = message.get('text', '')

    if text:
        if text.startswith('/'):
            return commandHandler.processMessage(data)
        else:
            return messageHandler.processMessage(data)
    
    # 4. Fallback for non-text messages (photos, voice, etc.)
    logging.info("Received a non-text update (e.g., photo or sticker)")
    return "OK", 200

if __name__ == '__main__':
    # Cloud Run provides a $PORT environment variable. Default to 8080.
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)