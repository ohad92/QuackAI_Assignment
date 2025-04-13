import sqlite3

def get_connection():
    return sqlite3.connect("articles.db")

def get_next_article_id():
    with get_connection() as conn:
        cur = conn.execute("SELECT id FROM articles ORDER BY id DESC")
        ids = cur.fetchall()
        if not ids:
            return "A1"
        last_id = ids[0][0]
        try:
            next_number = int(last_id[1:]) + 1
            return f"A{next_number}"
        except ValueError:
            return "A1"

def article_exists(article_id):
    with get_connection() as conn:
        cur = conn.execute("SELECT 1 FROM articles WHERE id = ?", (article_id,))
        return cur.fetchone() is not None

def insert_article(title, content, tags):
    article_id = get_next_article_id()
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO articles (id, title, content, tags) VALUES (?, ?, ?, ?)
        """, (article_id, title, content, ",".join(tags)))

def modify_article(article_id, field, value):
    if field == "tags":
        value = ",".join([v.strip() for v in value.split(",")])
    with get_connection() as conn:
        conn.execute(f"""
            UPDATE articles SET {field} = ? WHERE id = ?
        """, (value, article_id))

def remove_article(article_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM articles WHERE id = ?", (article_id,))

def find_articles_by_keyword(keyword):
    with get_connection() as conn:
        cur = conn.execute("""
            SELECT * FROM articles WHERE title LIKE ? OR content LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))
        return cur.fetchall()

def find_articles_by_tag(tag):
    with get_connection() as conn:
        cur = conn.execute("""
            SELECT * FROM articles WHERE tags LIKE ?
        """, (f"%{tag}%",))
        return cur.fetchall()

def get_all_articles():
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM articles")
        return cur.fetchall()