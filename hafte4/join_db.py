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
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT    NOT NULL,
            mande INTEGER NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kharid (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            moshtari_id  INTEGER NOT NULL,
            kala_id      INTEGER NOT NULL,
            mablagh      INTEGER NOT NULL
        )
    """)
    
    conn.commit()
    print("tables sakhte shadan!")
def add_kala(conn, name, ayar, vazn, gheymat):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO kala (name, ayar, vazn, gheymat) VALUES (?, ?, ?, ?)",
        (name, ayar, vazn, gheymat)
    )
    conn.commit()

def add_moshtari(conn, name, mande):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO moshtari (name, mande) VALUES (?, ?)",
        (name, mande)
    )
    conn.commit()

def add_kharid(conn, moshtari_id, kala_id, mablagh):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kharid (moshtari_id, kala_id, mablagh) VALUES (?, ?, ?)",(moshtari_id, kala_id, mablagh))
    conn.commit()

def get_kharid_moshtari(conn,moshtari_id):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT moshtari.name, kala.name, kharid.mablagh
    FROM kharid
    JOIN moshtari ON kharid.moshtari_id = moshtari.id
    JOIN kala ON kharid.kala_id = kala.id
    WHERE moshtari_id = ?
    """,(moshtari_id,))
    return cursor.fetchall()
def get_all_kharid(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT moshtari.name, kala.name, kharid.mablagh
    FROM kharid
    JOIN moshtari ON kharid.moshtari_id = moshtari.id
    JOIN kala ON kharid.kala_id = kala.id
    """)
    return cursor.fetchall()
def get_kharid_kala(conn, kala_id):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT moshtari.name, kala.name, kharid.mablagh
    FROM kharid
    JOIN moshtari ON kharid.moshtari_id = moshtari.id
    JOIN kala ON kharid.kala_id = kala.id WHERE kala.id = ?
    """,(kala_id,))
    return cursor.fetchall()


conn = sqlite3.connect("join_tala.db")
setup_db(conn)

add_kala(conn, "gilazar", 750, 10.5, 35000000)
add_kala(conn, "sekke", 900, 4.0, 50000000)
add_moshtari(conn, "Ahmadi", 5000000000)
add_moshtari(conn, "Rezaei", 3000000000)

add_kharid(conn, 1, 1, 350000000)    # Ahmadi gilazar kharid
add_kharid(conn, 1, 2, 200000000)    # Ahmadi sekke kharid
add_kharid(conn, 2, 1, 350000000)    # Rezaei gilazar kharid

print("kharid-haye Ahmadi:")
for row in get_kharid_moshtari(conn, 1):
    print(row)

print("\nkharid-haye Rezaei:")
for row in get_kharid_moshtari(conn, 2):
    print(row)
print("hame kharid-ha:")
for row in get_all_kharid(conn):
    print(row)

print("\nkasi ke gilazar (id=1) kharid:")
for row in get_kharid_kala(conn, 1):
    print(row)
conn.close()