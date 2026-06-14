from decimal import Decimal
print("mablaghe kharid ra vared konid:")
mablaghe_kharid = Decimal(input())
if mablaghe_kharid > 1000000:
    takhfif = mablaghe_kharid * 15 / 100
elif mablaghe_kharid >500000:
    takhfif = mablaghe_kharid * 10 / 100
elif mablaghe_kharid > 200000:
    takhfif = mablaghe_kharid * 5 / 100 
else:
    takhfif = Decimal("0")
mablaghe_nahae = mablaghe_kharid - takhfif
print(f"takhfife shoma:{takhfif.quantize(Decimal("0.01"))}")
print(f"mablaghe faktor shoma:{mablaghe_nahae.quantize(Decimal("0.01"))}")
