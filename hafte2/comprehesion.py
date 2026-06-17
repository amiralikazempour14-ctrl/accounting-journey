from decimal import Decimal
anbar = [
    {"nam": "abshode",  "ayar": 750, "vazn": Decimal("12.5"), "gheymat_geram": Decimal("30000000")},
    {"nam": "dastband", "ayar": 750, "vazn": Decimal("8.0"),  "gheymat_geram": Decimal("30000000")},
    {"nam": "sekke",    "ayar": 900, "vazn": Decimal("4.0"),  "gheymat_geram": Decimal("45000000")},
    {"nam": "shemsh",   "ayar": 995, "vazn": Decimal("20.0"), "gheymat_geram": Decimal("50000000")},
]
def arzeshe_anbar(anbar, ayar = 750):
    arzesh_koli = [g["vazn"] * g["gheymat_geram"] for g in anbar if g["ayar"] == ayar]
    return sum(arzesh_koli).quantize(Decimal("0.01"))
print(arzeshe_anbar(anbar, 900)) 