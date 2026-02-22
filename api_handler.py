# api_handler.py
import os
import logging
from google import genai
from google.genai import types
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

class ChatBackend:
    def __init__(self):
        try:
            # Initialize the new genai Client
            self.client = genai.Client(api_key=API_KEY)
            
            # Start a chat session using the new configuration format
            self.chat_session = self.client.chats.create(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=CAREER_ADVISOR_PROMPT,
                    temperature=0.7
                )
            )
            logger.info("Gemini API initialized successfully.")
        except Exception as e:
            logger.error(f"Initialization error: {e}")
            raise

    def get_response(self, user_input):
        try:
            logger.info("Sending request to Gemini API...")
            # The send_message method remains largely the same
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            logger.error(f"API Call Failed: {e}")
            return "I am currently experiencing technical difficulties. Please try again later."