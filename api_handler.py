# api_handler.py
import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import CAREER_ADVISOR_PROMPT

# Logging of API calls and errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Secure API key management
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing API Key. Check .env file.")

genai.configure(api_key=API_KEY)

class ChatBackend:
    def __init__(self):
        try:
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=CAREER_ADVISOR_PROMPT
            )
            # Maintain structured chat history
            self.chat_session = self.model.start_chat(history=[])
            logger.info("Gemini API initialized successfully.")
        except Exception as e:
            logger.error(f"Initialization error: {e}")
            raise

    def get_response(self, user_input):
        try:
            logger.info("Sending request to Gemini API...")
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            logger.error(f"API Call Failed: {e}")
            # Proper exception handling and fallback mechanism
            return "I am currently experiencing technical difficulties. Please try again later."