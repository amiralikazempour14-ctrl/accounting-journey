import sqlite3
conn = sqlite3.connect("moshtari.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS moshtari(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
mande INTEGER NOT NULL
)
""")
conn.commit()
print("jadval sakhte shod")


cursor.execute("INSERT INTO moshtari (name, mande) VALUES(?, ?)",
("amirali", 150000000))
cursor.execute("INSERT INTO moshtari (name, mande) VALUES(?, ?)",
("ali", 120000000))
conn.commit()
print("be jadval ezafe shod")

cursor.execute("SELECT * FROM moshtari")
print(cursor.fetchall())
conn.commit()

cursor.execute("UPDATE moshtari SET mande = ? WHERE id = ?", (100000, 2))
conn.commit()

cursor.execute("DELETE FROM moshtari WHERE id = ?", (1,))
conn.commit()

cursor.execute("SELECT * FROM moshtari")
for raw in cursor.fetchall():
    print(raw)