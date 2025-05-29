from scrapers.reddit_scraper import fetch_reddit_posts
from utils.sentiment_llm import analyze_text
from db.database import init_db
import sqlite3
from datetime import datetime
# Placeholder for scraper using PRAW or requests
def process_signals():
    posts = fetch_reddit_posts()
    conn = sqlite3.connect("evaqomp.db")
    cursor = conn.cursor()
    for post in posts:
        analysis = analyze_text(post)
        cursor.execute('''
            INSERT INTO signals (timestamp, source, text, tickers, sentiment, summary)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            datetime.utcnow().isoformat(),
            "Reddit",
            post,
            ','.join(analysis["tickers"]),
            analysis["sentiment"],
            analysis["summary"]
        ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    process_signals()
