from decimal import Decimal
anbar = [
    {"name": "gold", "vazn": Decimal("12.5"), "gheymat": Decimal("16500")},
    {"name": "dollar", "tedad": 1200, "gheymat": Decimal("155")},
    {"name": "sekke", "tedad": 3, "gheymat": Decimal("150000")}
]
bishtarin_gheimat = Decimal("0")
for kala in anbar:
    if "vazn" in kala:
        gheymat = kala["vazn"] * kala["gheymat"]
        if gheymat > bishtarin_gheimat:
            bishtarin_gheimat = gheymat
    else:
        gheymat = kala["tedad"] * kala["gheymat"]
        if gheymat > bishtarin_gheimat:
            bishtarin_gheimat = gheymat

print(bishtarin_gheimat)