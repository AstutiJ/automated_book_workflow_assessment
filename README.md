# 📚 Automated Book Workflow Assessment

This project automates the end-to-end book publishing pipeline using AI agents, human feedback, and reinforcement learning — designed as a smart system for rapid content generation, review, and refinement.

> 🚀 Built using: Python · Playwright · OpenAI LLMs · ChromaDB · Humanloop · FastAPI · Reinforcement Learning

---

## 💡 Project Objective

To streamline and accelerate the book creation process by combining:
- Web scraping
- AI-driven chapter generation
- Human-in-the-loop content refinement
- Feedback-aware learning through reinforcement

---

## 🧠 Core Features

| Feature | Description |
|--------|-------------|
| 🕸️ Web Scraping | Extracts content and screenshots using **Playwright** |
| ✍️ Chapter Generation | Uses **OpenAI GPT-based models** to write coherent chapters |
| 🧪 Human Review Loop | Integrates **Humanloop** for real-time human editing feedback |
| 🔁 Reinforcement Agent | Optimizes content quality based on user feedback |
| 🎙️ Voice + Semantic Search | Uses **embedding + ChromaDB** for natural search over content |
| 📦 Modular Structure | Split into scalable components (scraper, writer, RL agent, etc.) |

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** – API & agent orchestration
- **Playwright** – Web scraping
- **OpenAI API** – LLM chapter generation
- **ChromaDB** – Semantic search over chapter contents
- **Humanloop** – Human feedback interface
- **Reinforcement Learning** – Reward-based agent training

---

## 🚀 How to Run the Project

steps:
  - step: 1
    title: Clone the repository
    commands:
      - git clone https://github.com/AstutiJ/automated_book_workflow_assessment.git
      - cd automated_book_workflow_assessment

  - step: 2
    title: Set up Python environment
    description: |
      It's recommended to use a virtual environment.
    commands:
      - python -m venv venv
      - venv\Scripts\activate  # Use source venv/bin/activate on Mac/Linux

  - step: 3
    title: Install all dependencies
    commands:
      - pip install --upgrade pip
      - pip install -r requirements.txt

  - step: 4
    title: Install Playwright and its dependencies
    commands:
      - playwright install
      - playwright install-deps  # For Linux only

  - step: 5
    title: Launch the FastAPI application
    commands:
      - Streamlit app: streamlit run app.py


