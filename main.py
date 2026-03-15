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

    message = data.get('message')
    if message:
        text = message.get('text')
        if text:
            if text.startswith('/'):  # Commands
                return commandHandler.processMessage(data)
            else: # Button & text responses
                return messageHandler.processMessage(data)
    
    print("Received a non-text update (e.g., photo or sticker)")
    return "OK", 200