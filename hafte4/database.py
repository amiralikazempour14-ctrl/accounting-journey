import sqlite3
conn = sqlite3.connect("tala.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kala (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
ayar INTEGER NOT NULL,
vazn REAL NOT NULL,
gheymat INTEGER NOT NULL
)
""")

conn.commit()
print("jadval saakhte shod!")

cursor.execute("INSERT INTO kala (name, ayar, vazn, gheymat) VALUES(?, ?, ?, ?)",
("gilazar", 750, 10.5, 165000000))
cursor.execute("INSERT INTO kala (name, ayar, vazn, gheymat) VALUES(?, ?, ?, ?)",
("gilanrey", 750, 12.5, 199000000))
cursor.execute("INSERT INTO kala (name, ayar, vazn, gheymat) VALUES(?, ?, ?, ?)",
("tamam", 900, 4.0, 1850000000))

cursor.execute("UPDATE kala SET vazn = ? WHERE id = ?",(15.46,1))
conn.commit()
print("UPDATE SHOD")

cursor.execute("SELECT * FROM kala WHERE id = ?", (1,))
print(cursor.fetchone)

cursor.execute("DELETE FROM kala WHERE id = ?", (2,))
conn.commit()
print("DELETE SHOD")
cursor.execute("SELECT * FROM kala")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.close()
