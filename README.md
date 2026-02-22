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
This application is deployed publicly on an AWS EC2 instance.

1. **Provisioning**: Launched an Ubuntu EC2 instance with public IP accessibility.
2. **Networking**: Configured a basic security group to ensure proper port exposure (Port 8501 for Streamlit).
3. **Environment Setup**: Cloned the repository and installed dependencies inside a Python virtual environment.
4. **Configuration**: Set up environment variable configuration securely via a `.env` file.
5. **Execution**: Started the application using background process execution (`nohup streamlit run app.py &`).
