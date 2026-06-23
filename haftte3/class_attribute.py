from decimal import Decimal
class Kala:
    def __init__(self, name, ayar, gheymat_geram, vazn):
        self.name = name  
        self.ayar = ayar 
        self.gheymat_geram = gheymat_geram 
        self.vazn = vazn
    def value(self):
        return self.ayar * self.vazn / 750 * self.gheymat_geram
class Faktor:
    shomare_sanad = 1001
    def __init__(self, moshtari):
        self.moshtari = moshtari
        self.shomare = Faktor.shomare_sanad
        Faktor.shomare_sanad += 1
        self.aghlam = []
    def add_kala(self, kala):
        self.aghlam.append(kala)
    def faktor_value(self):
        total = Decimal("0")
        for kala in self.aghlam:
            total += kala.value()
        return total
    def __str__(self):
        return f"shomare sanad: {self.shomare} - name moshtari: {self.moshtari} - tedad kala: {len(self.aghlam)}"

f1 = Faktor("Ahmadi")        # shomare 1001
f1.add_kala(Kala("abshode", Decimal("30000000"), Decimal("10"), 750))
f1.add_kala(Kala("dastband", Decimal("30000000"), Decimal("5"), 750))

f2 = Faktor("Rezaei")        # shomare 1002
f2.add_kala(Kala("sekke_tala", Decimal("40000000"), Decimal("8"), 900))

print(f1)                    # shomare 1001, moshtari Ahmadi, 2 ghelam
print(f1.faktor_value())   # 450000000
print(f2)                    # shomare 1002