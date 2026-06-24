from decimal import Decimal
class Kala:
    def __init__(self, name, vazn, ayar):
        self._name = name
        self._ayar = ayar
        self._vazn = vazn
    def set_vazn(self, vazn):
        if vazn <= 0:
            print("ERROR")
            return
        self._vazn = vazn
    def set_ayar(self, ayar):
        if ayar <= 0 or ayar >= 1000:
            print("ERROR")
            return
        self._ayar = ayar
    def arzesh(self, gheymat_geram):
        return self._vazn * self._ayar / 750 * gheymat_geram
    def __str__(self):
        return f"name azmayeshgah: {self._name} - ayar: {self._ayar} - vazn: {self._vazn}"
class Anbar:
    def __init__(self, name):
        self._name = name
        self._aghlam = []
    def add_kala(self, kala):
        if not isinstance(kala, Kala):
            print("ERROR")
            return
        self._aghlam.append(kala)
    def arzesh_kol(self, gheymat_geram):
        total = Decimal("0")
        for kala in self._aghlam:
            total += kala.arzesh(gheymat_geram)
        return total
    def geran_tarin(self, gheymat_geram):
        exp = Decimal("0")
        for kala in self._aghlam:
            if kala.arzesh(gheymat_geram) > exp:
                exp = kala.arzesh(gheymat_geram)
            return exp
    def __str__(self):
        return f"name: {self._name} - tedad: {len(self._aghlam)}"
    
# ===== TEST =====
a = Anbar("Tehran")

# add_kala test:
a.add_kala(Kala("abshode", Decimal("10"), 750))
a.add_kala(Kala("dastband", Decimal("5"), 900))
a.add_kala("salam")                              # bayad ERROR bde
a.add_kala(Kala("sekke", Decimal("20"), 750))

# print anbar:
print(a)

# arzesh_kol:
print(a.arzesh_kol(Decimal("30000000")))         # bayad 1080000000 bde

# geran_tarin:
print(a.geran_tarin(Decimal("30000000")))         # bayad "sekke" bde

# validation test:
k = a._aghlam[0]     # abshode
k.set_vazn(Decimal("-5"))     # bayad ERROR bde
k.set_ayar(2000)              # bayad ERROR bde
k.set_vazn(Decimal("15"))     # ok — vazn mishe 15
print(k)                      # vazn bayad 15 bashe