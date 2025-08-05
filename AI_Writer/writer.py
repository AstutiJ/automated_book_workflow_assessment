# AI_Writer/writer.py

import os
from dotenv import load_dotenv
from loguru import logger
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=API_KEY)

def read_chapter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def spin_text_with_gemini(input_text):
    logger.info("Sending text to Gemini for rewriting...")

    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # ✅ updated model name

        prompt = (
            "You're an AI writer. Rewrite the following book chapter in a more creative, modern tone while preserving the story.\n\n"
            f"{input_text}"
        )

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        logger.error(f"Gemini API error: {e}")
        return None

def save_output(text, filename="chapter1_ai_written.txt"):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
        logger.success(f"Rewritten chapter saved as {filename}")

def generate_spun_chapter(input_file="chapter1_raw.txt"):
    raw_text = read_chapter(input_file)
    rewritten = spin_text_with_gemini(raw_text)

    if rewritten:
        save_output(rewritten)
    else:
        logger.error("Failed to get rewritten text from Gemini.")

if __name__ == "__main__":
    generate_spun_chapter()
