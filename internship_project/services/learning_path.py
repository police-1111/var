import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Instantiate Gemini 2.0 Flash
model = genai.GenerativeModel("gemini-2.0-flash")

def suggest_learning_path(topic: str) -> str:
    try:
        prompt = f"""
Create a clear, structured learning path for the topic: {topic}. 
Include beginner, intermediate, and advanced steps.
Format the response with headings for each level.
"""
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Request failed: {str(e)}"

# Example usage
if __name__ == "__main__":
    topic = "AI and Machine Learning"
    print(suggest_learning_path(topic))
