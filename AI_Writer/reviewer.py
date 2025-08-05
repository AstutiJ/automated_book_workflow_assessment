# AI_Reviewer/reviewer.py

import os
from dotenv import load_dotenv
from loguru import logger
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=API_KEY)

def read_ai_written_chapter(file_path="chapter1_ai_written.txt"):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def review_chapter(content):
    logger.info("Sending AI-written chapter to Gemini for review...")

    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        prompt = (
    "You are an expert editor reviewing an AI-generated chapter.\n"
    "Please provide feedback in the following **strict format**:\n\n"
    "=== FEEDBACK START ===\n"
    "1. Clarity and coherence:\n- <Your feedback>\n\n"
    "2. Tone and creativity:\n- <Your feedback>\n\n"
    "3. Grammar and correctness:\n- <Your feedback>\n\n"
    "4. Suggestions for improvement:\n- <Your suggestions>\n\n"
    "5. Overall Rating (out of 10): <Numeric score>\n"
    "=== FEEDBACK END ===\n\n"
    "Now review the following chapter:\n"
    f"{content}"
)

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        logger.error(f"Gemini Reviewer Error: {e}")
        return None

def save_review(text, filename="chapter1_ai_review.txt"):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
        logger.success(f"Review feedback saved as {filename}")

def generate_review():
    ai_content = read_ai_written_chapter()
    feedback = review_chapter(ai_content)

    if feedback:
        save_review(feedback)
    else:
        logger.error("Review generation failed.")

if __name__ == "__main__":
    generate_review()
