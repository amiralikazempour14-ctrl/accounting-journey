from decimal import Decimal
moshtari = {"name": "amirali", "mande": Decimal("50000")}
print(f"mandeye shoma:{moshtari.get("mande")}")
print("meghdar kharid khod ra vared konid")
kharid_jadid = Decimal(input())
mande_nahae = moshtari.get("mande") - kharid_jadid
moshtari["mande"] = mande_nahae
print(f"mande naha e shoma:{moshtari.get("mande")}")