# main.py

import os
import asyncio
import logging
from Playwright_Scraper.scraper import scrape_content, take_screenshot
from AI_Writer.writer import generate_spun_chapter
from AI_Writer.reviewer import generate_review
from Humanloop_interface.feedback_collector import main as collect_feedback

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

CHAPTER_URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
CHAPTER_RAW_FILE = "chapter1_raw.txt"
SCREENSHOT_FILE = "chapter_screenshot.png"

def step1_scrape_and_screenshot():
    logging.info("=== Step 1: Scraping and Screenshot ===")
    try:
        chapter_text = scrape_content(CHAPTER_URL)
        with open(CHAPTER_RAW_FILE, "w", encoding="utf-8") as f:
            f.write(chapter_text)
        logging.info("✅ Chapter text saved.")

        asyncio.run(take_screenshot(CHAPTER_URL, SCREENSHOT_FILE))
        logging.info("✅ Screenshot captured.")

    except Exception as e:
        logging.error(f"❌ Error in scraping/screenshot: {e}")
        return False
    return True

def step2_generate_draft():
    logging.info("=== Step 2: Generate AI Draft ===")
    try:
        generate_spun_chapter(CHAPTER_RAW_FILE)
        logging.info("✅ AI draft written.")
    except Exception as e:
        logging.error(f"❌ Failed to generate AI draft: {e}")
        return False
    return True

def step3_review_draft():
    logging.info("=== Step 3: Review AI Draft ===")
    try:
        generate_review()
        logging.info("✅ Review completed.")
    except Exception as e:
        logging.error(f"❌ Failed to review draft: {e}")
        return False
    return True

def step4_collect_human_feedback():
    logging.info("=== Step 4: Collect Human Feedback ===")
    try:
        collect_feedback()
    except Exception as e:
        logging.error(f"❌ Failed to collect human feedback: {e}")
        return False
    return True

def main():
    logging.info("\n=== 🚀 Automated Book Workflow Starting ===\n")

    if not step1_scrape_and_screenshot():
        return

    if not step2_generate_draft():
        return

    if not step3_review_draft():
        return

    if not step4_collect_human_feedback():
        return

    logging.info("\n=== ✅ Workflow Successfully Completed ===\n")

if __name__ == "__main__":
    main()
