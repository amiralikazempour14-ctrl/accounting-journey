from decimal import Decimal
print("gheimat ra vared konid:")
gheimate_kala = Decimal(input(""))
print("tedad kala ra vared konid:")
tedad_kala = int(input())
maliat_bar_arzeshe_afzoode = gheimate_kala * Decimal("0.09")
mablaghe_kol_kala = gheimate_kala + maliat_bar_arzeshe_afzoode
mablaghe_factor = mablaghe_kol_kala * tedad_kala
mablaghe_factor = mablaghe_factor.quantize(Decimal("0.01"))
print(f"gheimate nahae factor shoma:{mablaghe_factor}")