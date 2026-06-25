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
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            moshtari_id INTEGER NOT NULL,
            kala_id     INTEGER NOT NULL,
            mablagh     INTEGER NOT NULL
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
    print(f"{name} ezafe shod!")

def add_moshtari(conn, name, mande):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO moshtari (name, mande) VALUES (?, ?)",
        (name, mande)
    )
    conn.commit()
    print(f"{name} ezafe shod!")

def sabt_kharid(conn, moshtari_id, kala_id):
    cursor = conn.cursor()
    # qadam 1: gheymat ro az kala bkhun
    cursor.execute("SELECT gheymat FROM kala WHERE id = ?", (kala_id,))
    kala = cursor.fetchone()
    if not kala:
        print("kala peyda nashod!")
        return
    mablagh = kala[0]
    # qadam 2: kharid ro INSERT kon
    cursor.execute(
        "INSERT INTO kharid (moshtari_id, kala_id, mablagh) VALUES (?, ?, ?)",
        (moshtari_id, kala_id, mablagh)
    )
    conn.commit()
    print(f"kharid sabt shod! mablagh: {mablagh}")

def get_kharid_moshtari(conn, moshtari_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT moshtari.name, kala.name, kharid.mablagh
        FROM kharid
        JOIN moshtari ON kharid.moshtari_id = moshtari.id
        JOIN kala ON kharid.kala_id = kala.id
        WHERE moshtari.id = ?
    """, (moshtari_id,))
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

# ===== MENU =====
conn = sqlite3.connect("challenge_join.db")
setup_db(conn)

while True:
    print("\n1) ezafe kala")
    print("2) ezafe moshtari")
    print("3) sabt kharid")
    print("4) kharid-haye ye moshtari")
    print("5) hame kharid-ha")
    print("6) khoruj")

    entekhab = input("entekhab: ")

    if entekhab == "1":
        name = input("name kala: ")
        ayar = int(input("ayar: "))
        vazn = float(input("vazn: "))
        gheymat = int(input("gheymat: "))
        add_kala(conn, name, ayar, vazn, gheymat)

    elif entekhab == "2":
        name = input("name moshtari: ")
        mande = int(input("mande: "))
        add_moshtari(conn, name, mande)

    elif entekhab == "3":
        moshtari_id = int(input("moshtari id: "))
        kala_id = int(input("kala id: "))
        sabt_kharid(conn, moshtari_id, kala_id)

    elif entekhab == "4":
        moshtari_id = int(input("moshtari id: "))
        rows = get_kharid_moshtari(conn, moshtari_id)
        if not rows:
            print("kharid vojod nadarad!")
        for row in rows:
            print(f"moshtari: {row[0]} | kala: {row[1]} | mablagh: {row[2]}")

    elif entekhab == "5":
        rows = get_all_kharid(conn)
        if not rows:
            print("kharid vojod nadarad!")
        for row in rows:
            print(f"moshtari: {row[0]} | kala: {row[1]} | mablagh: {row[2]}")

    elif entekhab == "6":
        print("khodafez!")
        break

    else:
        print("entekhab ghalat!")

conn.close()