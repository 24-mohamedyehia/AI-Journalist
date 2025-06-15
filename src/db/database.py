import sqlite3
from datetime import datetime

data_path = 'src/db/articels.db'

class Database:
    def __init__(self, db_path=data_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            article TEXT,
            date TEXT
        )""")
        self.conn.commit()

    def insert_article(self, topic, article):
        date = datetime.now().isoformat()
        self.cursor.execute(
            "INSERT INTO articles (topic, article, date) VALUES (?, ?, ?)",
            (topic, article, date)
        )
        self.conn.commit()

    def get_all_articles(self):
        self.cursor.execute("SELECT id, topic, date FROM articles ORDER BY date DESC")
        return self.cursor.fetchall()

    def get_article_by_id(self, article_id):
        self.cursor.execute("SELECT id, topic, article, date FROM articles WHERE id = ?", (article_id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()