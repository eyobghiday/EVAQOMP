import sqlite3
# Databse placeholder
def init_db():
    conn = sqlite3.connect("evaqomp.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source TEXT,
            text TEXT,
            tickers TEXT,
            sentiment TEXT,
            summary TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_all_signals():
    conn = sqlite3.connect("evaqomp.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM signals")
    rows = cursor.fetchall()
    conn.close()
    return rows
