
import os

from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

KWTA_SYSTEM_RULES = """You are the official AI Assistant for Kim Warwick Tennis Academy (KWTA) in Hornsby. 
Rules:
1. ONLY use info from kwta.com.au.
2. CRITICAL: Your response must be 1-2 sentences maximum, like a quick text message.
3. Be professional but very concise.
4. Never tell users to 'check the website'. Provide the direct answer or (02) 9477-6377 / reception@kwta.com.au.
5. Do not use bolding or complex formatting; keep it plain text for a mobile screen."""

def get_gemini_response(user_query):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=user_query,
        config=types.GenerateContentConfig(
            system_instruction=KWTA_SYSTEM_RULES,
            max_output_tokens=800, # Safety buffer for Telegram limits
            temperature=0.3, # Lower temperature = more factual/less 'wordy'
        )
    )
    return response.text


def process_message()