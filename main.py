from flask import Flask, request
import json
import logging
import os

from handlers import messageHandler, commandHandler, buttonHandler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    print("Application startup complete")
    data = request.get_json(force=True)

    print((f"Incoming Update: {data}"))
    if 'callback_query' in data:
        return buttonHandler.processMessage(data)

    message = data.get('message')
    if message:
        text = message.get('text')
        if text:
            if text.startswith('/'):
                return commandHandler.processMessage(data)
            else:
                return messageHandler.processMessage(data)
    
    print("Received a non-text update (e.g., photo or sticker)")
    return "OK", 200