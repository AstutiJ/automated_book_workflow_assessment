# scraper.py

from bs4 import BeautifulSoup
import requests
from loguru import logger
import asyncio
from playwright.async_api import async_playwright

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

def scrape_content(url):
    logger.info(f"Scraping content from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    content_div = soup.find("div", class_="mw-parser-output")
    paragraphs = content_div.find_all("p")
    text = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    return text


async def take_screenshot(url, output_file="chapter_screenshot.png"):
    logger.info("Taking screenshot of the chapter page")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.screenshot(path=output_file, full_page=True)
        await browser.close()
        logger.info(f"Screenshot saved as {output_file}")


if __name__ == "__main__":
    logger.info("Starting scraping process...")
    chapter_text = scrape_content(URL)
    
    with open("chapter1_raw.txt", "w", encoding="utf-8") as f:
        f.write(chapter_text)
        logger.success("Chapter text saved as chapter1_raw.txt")

    asyncio.run(take_screenshot(URL))
