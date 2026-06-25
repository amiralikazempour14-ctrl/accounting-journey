import sqlite3

def setup_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kala (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        ayar    INTEGER NOT NULL,
        vazn    REAL    NOT NULL,
        gheymat INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS moshtari (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    mande       INTEGER NOT NULL
    )
    """)
    conn.commit()
    print("TABLE SAKHTE SHOD!")
def add_kala(conn, name, ayar, vazn, gheymat):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kala (name, ayar, vazn, gheymat) VALUES (?, ?, ?, ?)",(name, ayar, vazn, gheymat))
    conn.commit()
    print("kala add shod")
def get_all_kala(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kala")
    return cursor.fetchall()
def add_moshtari(conn, name, mande):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO moshtari (name, mande) VALUES (?, ?)",(name, mande))
    conn.commit()
    print("moshtari add shod")
def get_all_moshtari(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moshtari")
    return cursor.fetchall()
def update_mande(conn, moshtari_id, mande_jadid):
    cursor = conn.cursor()
    cursor.execute("UPDATE moshtari SET mande = ? WHERE id = ?",(mande_jadid, moshtari_id))
    conn.commit()
def get_moshtari(conn, moshtari_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moshtari WHERE id = ?",(moshtari_id,))
    return cursor.fetchone()
def delete_kala(conn, kala_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kala WHERE id = ?",(kala_id,))
    conn.commit()
    print("DELETE SHOD!")
def geran_tarin(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kala ORDER BY gheymat DESC LIMIT 1")
    return cursor.fetchone()
def kala_ayar(conn, ayar):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kala WHERE ayar = ?",(ayar,))
    return cursor.fetchall()


conn = sqlite3.connect("tala_system.db")
setup_db(conn)

add_kala(conn, "gillazar", 750, 10.65, 159000000)
add_kala(conn, "gilanrey", 753, 40.56, 162000000)
add_moshtari(conn, "amirali", 200000000000)

for k in get_all_kala(conn):
    print(k)

for m in get_all_moshtari(conn):
    print(m)

update_mande(conn, 1, 250000000000)
print(get_moshtari(conn, 1))
delete_kala(conn, 2)
for a in get_all_kala(conn):
    print(a)
print(geran_tarin(conn))
for i in kala_ayar(conn, 750):
    print(i)
conn.close()
