
import google.generativeai as genai
import os

# Setup your client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

KWTA_SYSTEM_RULES = """You are the official AI Assistant for Kim Warwick Tennis Academy (KWTA) in Hornsby. 
CRITICAL: Your response must be under 3,000 characters to fit Telegram limits. 
Rules:
1. Only use information from kwta.com.au. Do not use outside knowledge.
2. Be concise and professional.
3. Never tell users to 'search the internet' or 'check the website'. Give the answer directly.
4. If info is missing, provide: (02) 9477-6377 or reception@kwta.com.au."""

# Initialize model with instructions (the modern way)
model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-lite-preview",
    system_instruction=KWTA_SYSTEM_RULES
)

def get_gemini_response(user_query):
    response = model.generate_content(user_query)
    return response.text