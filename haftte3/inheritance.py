from decimal import Decimal

class Kala:                                    # PARENT (paye)
    def __init__(self, name, gheymat_geram):
        self.name = name
        self.gheymat_geram = gheymat_geram
    def value(self):
        return Decimal("0")

class Abshode(Kala):                           # CHILD
    def __init__(self, name, gheymat_geram, ayar, vazn):
        super().__init__(name, gheymat_geram)  # bedoone self!
        self.ayar = ayar
        self.vazn = vazn
    def value(self):                           # override
        return self.vazn * self.ayar / 750 * self.gheymat_geram   # self, na super

class Sekke(Kala):                             # CHILD
    def __init__(self, name, gheymat_geram, tedad):
        super().__init__(name, gheymat_geram)
        self.tedad = tedad
    def value(self):                           # override
        return self.tedad * self.gheymat_geram

class Anbar:                                   # negahdarande-ye list-e markab
    def __init__(self):
        self.aghlam = []
    def add_kala(self, kala):
        self.aghlam.append(kala)
    def arzesh_kol(self):
        value_kol = Decimal("0")               # ghabl az halqe!
        for kala in self.aghlam:
            value_kol += kala.value()          # polymorphism: har kodum value-ye KHODESH
        return value_kol

# ---- test ----
anbar = Anbar()
anbar.add_kala(Abshode("abshode", Decimal("30000000"), 750, Decimal("10")))
anbar.add_kala(Sekke("sekke", Decimal("50000000"), 3))

for kala in anbar.aghlam:
    print(f"{kala.name} - arzesh: {kala.value()}")

print(f"arzesh kol: {anbar.arzesh_kol()}")