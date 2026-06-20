from decimal import Decimal

class Kala:
    def __init__(self, nam, ayar, vazn):
        self.nam = nam
        self.ayar = ayar
        self.vazn = vazn
    def gheimat(self, gheymat_geram):
        return self.vazn * self.ayar / 750 * gheymat_geram

class Moshtari:
    def __init__(self, nam, mande):
        self.nam = nam
        self.mande = mande
    def kharid(self, mablagh):
        self.mande -= mablagh
    def __str__(self):
        return f"{self.nam} - mande: {self.mande}"
class Faktor:
    def __init__(self,moshtari):
        self.moshtari = moshtari
        self.aghlam = []
    def addkala(self, kala):
        self.aghlam.append(kala)
    def jam_e_kol(self, gheymate_geram):
        total = Decimal("0")
        for kala in self.aghlam:
            total += kala.gheimat(gheymate_geram)
        return total.quantize(Decimal("0.01"))
    def nahae_kardan(self, gheymat_geram):
        total = self.jam_e_kol(gheymat_geram)
        total = self.moshtari.kharid(total)
        return total

m = Moshtari("amirali", Decimal("120000000"))
f = Faktor(m)
f.addkala(Kala("GILAZAR", 748, Decimal("35.65")))
f.addkala(Kala("GILAN REY", 752, Decimal("20.84")))
print(len(f.aghlam))
print(f.jam_e_kol(Decimal("15500000")))
f.nahae_kardan(Decimal("15500000"))
print(m)

#=======================================
