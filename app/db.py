import sqlite3
import json
import os

def initialize_db():
    with sqlite3.connect("articles.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT
            )
        """)
        cur = conn.execute("SELECT COUNT(*) FROM articles")
        count = cur.fetchone()[0]
        if count == 0:
            populate_from_json(conn)

def populate_from_json(conn):
    if not os.path.exists("Articles.json"):
        print("Articles.json not found. Skipping initial data load.")
        return

    with open("Articles.json", "r") as f:
        data = json.load(f)
        for article in data.get("articles", []):
            id = article.get("id", "").strip()
            title = article.get("title", "").strip()
            content = article.get("content", "").strip()
            tags = article.get("tags", [])

            if not (id and title and content and isinstance(tags, list)):
                continue  # Skip invalid entries

            tags_str = ",".join([tag.strip() for tag in tags])
            conn.execute("""
                INSERT INTO articles (id, title, content, tags) VALUES (?, ?, ?, ?)
            """, (id, title, content, tags_str))
