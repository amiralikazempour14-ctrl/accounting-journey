from decimal import Decimal
import sqlite3

class Kala:
    def __init__(self, name, gheymat, vazn, ayar):
        self.id = None
        self._name = name
        self._gheymat = gheymat
        self._vazn = vazn
        self._ayar = ayar

    def arzesh(self):
        return self._vazn * self._ayar / 750 * self._gheymat

    def __str__(self):
        return f"[{self.id}] {self._name} arzesh: {self.arzesh()}"


class KalaRepository:
    def __init__(self, conn):
        self.conn = conn

    def save(self, kala):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO kala (name, gheymat, vazn, ayar) VALUES (?, ?, ?, ?)",
            (kala._name, kala._gheymat, float(kala._vazn), kala._ayar)
        )
        self.conn.commit()
        kala.id = cursor.lastrowid
        return kala

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM kala")
        result = []
        for row in cursor.fetchall():
            kala = Kala(row[1], row[2], row[3], row[4])
            kala.id = row[0]
            result.append(kala)
        return result

    def get_by_id(self, kala_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM kala WHERE id = ?", (kala_id,))
        row = cursor.fetchone()
        if not row:
            return None
        kala = Kala(row[1], row[2], row[3], row[4])
        kala.id = row[0]
        return kala


class Moshtari:
    def __init__(self, name, mande):
        self.id = None
        self._name = name
        self._mande = mande

    def kharid(self, mablagh):
        if mablagh > self._mande:
            print("mande kafi nist!")
            return False
        self._mande -= mablagh
        return True

    def __str__(self):
        return f"[{self.id}] {self._name} - mande: {self._mande}"


class MoshtariRepository:
    def __init__(self, conn):
        self.conn = conn

    def save(self, moshtari):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO moshtari (name, mande) VALUES (?, ?)",
            (moshtari._name, moshtari._mande)
        )
        self.conn.commit()
        moshtari.id = cursor.lastrowid
        return moshtari

    def update_mande(self, moshtari):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE moshtari SET mande = ? WHERE id = ?",
            (moshtari._mande, moshtari.id)
        )
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM moshtari")
        result = []
        for row in cursor.fetchall():
            m = Moshtari(row[1], row[2])
            m.id = row[0]
            result.append(m)
        return result


# ===== SETUP =====
conn = sqlite3.connect("tala_oop.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS kala (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    gheymat INTEGER NOT NULL,
    vazn    REAL    NOT NULL,
    ayar    INTEGER NOT NULL
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS moshtari (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    mande INTEGER NOT NULL
)""")
conn.commit()

# ===== TEST =====
repo = KalaRepository(conn)
k1 = Kala("gilazar", 35000000, Decimal("10.5"), 750)
k2 = Kala("sekke", 50000000, Decimal("4.0"), 900)
repo.save(k1)
repo.save(k2)

print("hame kala-ha:")
for k in repo.get_all():
    print(k)

print("\nget_by_id=1:")
k = repo.get_by_id(1)
print(k)
print(k.arzesh())

m_repo = MoshtariRepository(conn)
m = Moshtari("Ahmadi", 5000000000)
m_repo.save(m)
print(f"\n{m}")

m.kharid(367500000)
m_repo.update_mande(m)

print("\nhame moshtari-ha:")
for moshtari in m_repo.get_all():
    print(moshtari)

conn.close()