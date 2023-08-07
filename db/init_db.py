import sqlite3

conn = sqlite3.connect('db/shorturls.db')

with open('db/schema.sql') as f:
    conn.executescript(f.read())
conn.execute("INSERT INTO urls (id, shorten_id, original_url, deletion_url) VALUES (100000000, 'RUtE', 'www.example.com', 'deletion12391028')")
conn.commit()
conn.close()