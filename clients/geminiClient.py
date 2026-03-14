
import os

from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

KWTA_SYSTEM_RULES = """You are the official AI Assistant for Kim Warwick Tennis Academy (KWTA) in Hornsby. 
CRITICAL: Your response must be under 3,000 characters to fit Telegram limits. 
Rules:
1. Only use information from kwta.com.au. Do not use outside knowledge.
2. Be concise and professional.
3. Never tell users to 'search the internet' or 'check the website'. Give the answer directly.
4. If info is missing, provide: (02) 9477-6377 or reception@kwta.com.au."""

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