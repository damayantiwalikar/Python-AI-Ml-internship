import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

print("✅ Gemini Chat Ready (type 'exit' to quit)\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break

    response = model.generate_content(question)
    print("Gemini:", response.text, "\n")