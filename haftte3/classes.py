from decimal import Decimal
class kala:
    def __init__(self, nam_azmayeshgah, weight, ayar):
        self.nam_azmayeshgah = nam_azmayeshgah
        self.weight = weight
        self.ayar = ayar
    def gheimat(self,gheimat_geram):
        return self.weight * self.ayar / 750 * gheimat_geram.quantize(Decimal("0.01"))
kala1 = kala("gil azar", Decimal("10.5"), 750)
kala2 = kala("gillan_rey", Decimal("15.65"), 970)
print(kala1.nam_azmayeshgah)
print(kala1.weight)
print(kala1.ayar)
print(kala1.gheimat(Decimal("10000")))
print(kala2.nam_azmayeshgah)
print(kala2.weight)
print(kala2.ayar)
print(kala2.gheimat(Decimal("10000")))