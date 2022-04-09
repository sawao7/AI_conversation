import sqlite3

conn = sqlite3.connect('TestDB.db')

c = conn.cursor()
c.execute("DELETE FROM Conversation")
conn.commit()
