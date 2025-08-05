import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
# app.py

import streamlit as st
import os
import asyncio

from Playwright_Scraper.scraper import scrape_content, take_screenshot
from AI_Writer.writer import generate_spun_chapter
from AI_Writer.reviewer import generate_review, read_ai_written_chapter
from Humanloop_interface.feedback_collector import log_feedback

RAW_FILE = "chapter1_raw.txt"
WRITTEN_FILE = "chapter1_ai_written.txt"
REVIEW_FILE = "chapter1_ai_review.txt"
SCREENSHOT = "chapter_screenshot.png"

st.set_page_config(page_title="📚 AI Book Workflow", layout="wide")
st.title("📘 AI Book Workflow Automation")

# URL Input
chapter_url = st.text_input("📖 Enter Chapter URL", value="https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

if st.button("🚀 Run Complete Workflow"):
    with st.spinner("🔍 Scraping content and capturing screenshot..."):
        try:
            content = scrape_content(chapter_url)
            with open(RAW_FILE, "w", encoding="utf-8") as f:
                f.write(content)
            asyncio.run(take_screenshot(chapter_url, SCREENSHOT))
            st.success("✅ Scraped and saved raw chapter.")

        except Exception as e:
            st.error(f"Scraping failed: {e}")
            st.stop()

    with st.spinner("📝 Rewriting with Gemini..."):
        try:
            generate_spun_chapter(RAW_FILE)
            st.success("✅ AI Draft Generated.")
        except Exception as e:
            st.error(f"Draft generation failed: {e}")
            st.stop()

    with st.spinner("🔍 Reviewing AI Draft..."):
        try:
            generate_review()
            st.success("✅ Review Completed.")
        except Exception as e:
            st.error(f"Review failed: {e}")
            st.stop()

# Display Results
if os.path.exists(RAW_FILE):
    st.subheader("📄 Raw Chapter (Scraped)")
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        st.text_area("Raw Chapter", f.read(), height=200)

if os.path.exists(WRITTEN_FILE):
    st.subheader("✍️ AI-Written Chapter")
    with open(WRITTEN_FILE, "r", encoding="utf-8") as f:
        st.text_area("AI Draft", f.read(), height=200)

if os.path.exists(REVIEW_FILE):
    st.subheader("📝 AI Review Feedback")
    with open(REVIEW_FILE, "r", encoding="utf-8") as f:
        st.text_area("Feedback", f.read(), height=200)

# Human Feedback Input
st.subheader("🧠 Your Feedback")
user_feedback = st.radio(
    "Do you accept the AI-written content?",
    ["Yes (Accept) ✅", "No (Reject) ❌", "Needs Manual Edits ✍️"]
)

if st.button("📩 Submit Feedback"):
    reward_map = {
        "Yes (Accept) ✅": 1,
        "No (Reject) ❌": -1,
        "Needs Manual Edits ✍️": 0
    }
    reward_value = reward_map[user_feedback]
    try:
        log_feedback(reward_value)
        st.success(f"✅ Feedback logged with reward: {reward_value}")
    except Exception as e:
        st.error(f"Failed to log feedback: {e}")
