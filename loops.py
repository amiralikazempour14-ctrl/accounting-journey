import random
from decimal import Decimal
rand = random.randint(1, 100)
adad_e_hads = int(input("adad ra hads bezanid"))
while adad_e_hads != rand:
    if adad_e_hads < rand:
        print("adad kuchek tar ast")
        adad_e_hads = int(input("adad jadid ra vared konid:"))
    elif adad_e_hads > rand:
        print("adad bozorg tar ast")
        adad_e_hads = int(input("adad jadid ra vared konid:"))

print(f"shoma dorost hads zadid ada {rand} bood.")