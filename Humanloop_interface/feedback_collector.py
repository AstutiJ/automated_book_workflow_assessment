# RL_Feedback/reward_collector.py

import os
import csv
from datetime import datetime

AI_WRITTEN_FILE = "chapter1_ai_written.txt"
AI_REVIEW_FILE = "chapter1_ai_review.txt"
OUTPUT_FILE = "feedback_log.csv"


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def ask_user_feedback():
    print("\n--- Human Feedback Time ---\n")
    print("Q1: Do you accept the AI-written content?")
    print("1. Yes (Accept) ✅")
    print("2. No (Reject) ❌")
    print("3. Needs Manual Edits ✍️")
    choice = input("Your response (1/2/3): ").strip()

    if choice == "1":
        return 1
    elif choice == "2":
        return -1
    elif choice == "3":
        return 0
    else:
        print("Invalid input. Please enter 1, 2 or 3.")
        return ask_user_feedback()


def log_feedback(reward_value):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data = {
        "timestamp": timestamp,
        "chapter": "chapter1",
        "reward": reward_value
    }

    file_exists = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=log_data.keys())

        if not file_exists:
            writer.writeheader()
        writer.writerow(log_data)

    print(f"\n✅ Feedback logged with reward = {reward_value}")


def main():
    print("\n========== AI-WRITTEN CHAPTER ==========\n")
    print(read_file(AI_WRITTEN_FILE)[:1000])  # Show only preview

    print("\n========== AI REVIEW FEEDBACK ==========\n")
    print(read_file(AI_REVIEW_FILE)[:1000])  # Show only preview

    reward = ask_user_feedback()
    log_feedback(reward)


if __name__ == "__main__":
    main()
