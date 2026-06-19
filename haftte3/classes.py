from decimal import Decimal
class moshtari:
    def __init__(self, name, mande):
        self.name = name
        self.mande = mande
    def kharid(self, mablagh):
        self.mande -= mablagh
        print(f"mablagh kharid shode={mablagh}")
        print(f"mande nahae={self.mande}")
    def pardakht(self, mablagh):
        self.mande += mablagh
        print(f"mablagh pardakht shode={mablagh}")
        print(f"mande nahae={self.mande}")
    def __str__(self):
        return f"name: {self.name}, mande: {self.mande}"
m = moshtari("amirali", Decimal("100000"))
m.kharid(Decimal("10000"))
m.pardakht(Decimal("100000"))
print(m)
