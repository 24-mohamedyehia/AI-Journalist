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

    def close(self):
        self.conn.close()