from decimal import Decimal

class Kala:
    def __init__(self, name, gheymat):
        self._name = name
        self._gheymat = gheymat
    def value(self):
        return Decimal("0")
    def __str__(self):
        return f"name: {self._name} - gheymate har geram: {self._gheymat}"

class Abshode(Kala):
    def __init__(self, name, gheymat, vazn, ayar):
        super().__init__(name, gheymat)
        self._vazn = vazn
        self._ayar = ayar
    def set_vazn(self, vazn):
        if vazn <= 0:
            print("ERROR: vazn bayad mosbat bashe")
            return
        self._vazn = vazn
    def set_ayar(self, ayar):
        if ayar <= 0 or ayar >= 1000:
            print("ERROR: ayar ghalat")
            return
        self._ayar = ayar
    def value(self):
        return self._gheymat * self._ayar * self._vazn / 750
    def __str__(self):
        return f"name: {self._name} - ayar: {self._ayar} - vazn: {self._vazn} - arzesh: {self.value()}"

class Sekke(Kala):
    def __init__(self, name, gheymat, tedad):
        super().__init__(name, gheymat)
        self._tedad = tedad
    def set_tedad(self, tedad):
        if tedad <= 0:
            print("ERROR: tedad bayad mosbat bashe")
            return
        self._tedad = tedad
    def value(self):
        return self._gheymat * self._tedad * 900 / 750
    def __str__(self):
        return f"name: {self._name} - tedad: {self._tedad} - arzesh: {self.value()}"

class Moshtari:
    def __init__(self, name, mande):
        self._name = name
        self._mande = mande
        self.history = []
    def kharid(self, mablagh):
        if mablagh > self._mande:
            print("ERROR: mande kafi nist")
            return
        self._mande -= mablagh
        self.history.append({"noe": "kharid", "mablagh": mablagh})
    def variz(self, mablagh):
        if mablagh <= 0:
            print("ERROR: mablagh bayad mosbat bashe")
            return
        self._mande += mablagh
        self.history.append({"noe": "variz", "mablagh": mablagh})
    def show_history(self):
        for item in self.history:
            print(f"{item['noe']}: {item['mablagh']}")
    def __str__(self):
        return f"{self._name} - mande: {self._mande}"

class Factor:
    shomare_sanad = 1001
    def __init__(self, moshtari):
        self._moshtari = moshtari
        self._shomare = Factor.shomare_sanad
        Factor.shomare_sanad += 1
        self._aghlam = []
    def add_kala(self, kala):
        if not isinstance(kala, Kala):
            print("ERROR: faqat Kala mishire")
            return
        self._aghlam.append(kala)
    def value_kol(self):
        total = Decimal("0")
        for kala in self._aghlam:
            total += kala.value()
        return total
    def nahae_kardan(self):
        total = self.value_kol()
        self._moshtari.kharid(total)
        return total
    def __str__(self):
        return f"shomare: {self._shomare} - moshtari: {self._moshtari._name} - tedad: {len(self._aghlam)}"

class Anbar:
    def __init__(self, name):
        self._name = name
        self._aghlam = []
    def add_kala(self, kala):
        if not isinstance(kala, Kala):
            print("ERROR: faqat Kala mishire")
            return
        self._aghlam.append(kala)
    def value_kol(self):
        total = Decimal("0")
        for kala in self._aghlam:
            total += kala.value()
        return total
    def geran_tarin(self):
        exp = self._aghlam[0]
        for kala in self._aghlam:
            if kala.value() > exp.value():
                exp = kala
        return exp._name
    def __str__(self):
        return f"anbar: {self._name} - tedad: {len(self._aghlam)}"

# ===== TEST =====
print("=" * 40)
print("TEST: Anbar")
print("=" * 40)
anbar = Anbar("Tehran")
anbar.add_kala(Abshode("gilazar", Decimal("35000000"), Decimal("10"), 750))
anbar.add_kala(Abshode("gilanrey", Decimal("35000000"), Decimal("5"), 900))
anbar.add_kala(Sekke("sekke tamam", Decimal("50000000"), 3))
anbar.add_kala("salam")              # ERROR
print(anbar)
print(f"arzesh kol: {anbar.value_kol()}")
print(f"geran tarin: {anbar.geran_tarin()}")

print("\n" + "=" * 40)
print("TEST: Moshtari")
print("=" * 40)
m = Moshtari("Ahmadi", Decimal("5000000000"))
m.variz(Decimal("1000000000"))
m.kharid(Decimal("500000000"))
m.kharid(Decimal("9999999999"))      # ERROR: mande kafi nist
print(m)
m.show_history()

print("\n" + "=" * 40)
print("TEST: Factor")
print("=" * 40)
f1 = Factor(m)
f1.add_kala(Abshode("abshode", Decimal("35000000"), Decimal("8"), 750))
f1.add_kala(Sekke("nim sekke", Decimal("25000000"), 2))
print(f1)
print(f"value kol: {f1.value_kol()}")
f1.nahae_kardan()
print(f"moshtari baad az faktor: {m}")

f2 = Factor(m)                        # shomare 1002
print(f"\n{f2}")                       # bbin shomare khودkar!

print("\n" + "=" * 40)
print("TEST: Validation")
print("=" * 40)
k = anbar._aghlam[0]
k.set_vazn(Decimal("-5"))             # ERROR
k.set_ayar(2000)                      # ERROR
k.set_vazn(Decimal("15"))             # ok
print(k)