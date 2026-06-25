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
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        mande   INTEGER NOT NULL
    )
    """)
    conn.commit()

def add_kala(conn, name, ayar, vazn, gheymat):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO kala (name, ayar, vazn, gheymat) VALUES (?, ?, ?, ?)",
        (name, ayar, vazn, gheymat)
    )
    conn.commit()
    print(f"{name} ezafe shod!")

def get_all_kala(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kala")
    return cursor.fetchall()

def add_moshtari(conn, name, mande):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO moshtari (name, mande) VALUES (?, ?)",
        (name, mande)
    )
    conn.commit()
    print(f"{name} ezafe shod!")

def get_all_moshtari(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moshtari")
    return cursor.fetchall()

def update_mande(conn, moshtari_id, mande_jadid):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE moshtari SET mande = ? WHERE id = ?",
        (mande_jadid, moshtari_id)
    )
    conn.commit()
    print("mande update shod!")

def geran_tarin(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kala ORDER BY gheymat DESC LIMIT 1")
    return cursor.fetchone()

# ===== MENU =====
conn = sqlite3.connect("challenge_tala.db")
setup_db(conn)

while True:
    print("\n1) ezafe kala")
    print("2) namayesh hame kala")
    print("3) ezafe moshtari")
    print("4) namayesh hame moshtari")
    print("5) update mande moshtari")
    print("6) geran tarin kala")
    print("7) khoruj")
    
    entekhab = input("entekhab: ")
    
    if entekhab == "1":
        name = input("name kala: ")
        ayar = int(input("ayar (masalan 750): "))
        vazn = float(input("vazn (gram): "))
        gheymat = int(input("gheymat (rial): "))
        add_kala(conn, name, ayar, vazn, gheymat)
    
    elif entekhab == "2":
        kala_ha = get_all_kala(conn)
        if not kala_ha:
            print("anbar khali ast!")
        for k in kala_ha:
            print(f"id:{k[0]} | name:{k[1]} | ayar:{k[2]} | vazn:{k[3]} | gheymat:{k[4]}")
    
    elif entekhab == "3":
        name = input("name moshtari: ")
        mande = int(input("mande (rial): "))
        add_moshtari(conn, name, mande)
    
    elif entekhab == "4":
        moshtari_ha = get_all_moshtari(conn)
        if not moshtari_ha:
            print("moshtari vojod nadarad!")
        for m in moshtari_ha:
            print(f"id:{m[0]} | name:{m[1]} | mande:{m[2]}")
    
    elif entekhab == "5":
        moshtari_id = int(input("id moshtari: "))
        mande_jadid = int(input("mande jadid (rial): "))
        update_mande(conn, moshtari_id, mande_jadid)
    
    elif entekhab == "6":
        k = geran_tarin(conn)
        if k:
            print(f"geran tarin: {k[1]} | gheymat: {k[4]}")
        else:
            print("anbar khali ast!")
    
    elif entekhab == "7":
        print("khodafez!")
        break
    
    else:
        print("entekhab ghalat!")

conn.close()