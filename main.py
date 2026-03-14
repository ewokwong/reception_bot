from flask import Flask, request
import json
import logging
import os

app = Flask(__name__)

# Configure logging to output to the console (which shows up in Cloud Run logs)
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    # 1. Get the JSON data from the request
    data = request.get_json(force=True)
    
    # 2. Log the request body (formatted for readability)
    logging.info("--- New Webhook Received ---")
    logging.info(f"Headers: {dict(request.headers)}")
    logging.info(f"Body: {json.dumps(data, indent=2)}")
    
    return "ok", 200

if __name__ == '__main__':
    # Cloud Run provides a $PORT environment variable. Default to 8080.
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)