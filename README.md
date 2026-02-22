# AI Career Advisor Chatbot

A production-ready, domain-specific chatbot powered by the Google Gemini GenAI API.

## Architecture Explanation
User -> UI (Streamlit) -> Backend Layer -> Prompt Engineering Module -> Gemini API -> Response Processing -> UI Rendering

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment and install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file in the root directory and add your API key: `GEMINI_API_KEY=your_api_key_here`
5. Run the application: `streamlit run app.py`

## Deployment
(We will document the AWS EC2 deployment steps here once completed).