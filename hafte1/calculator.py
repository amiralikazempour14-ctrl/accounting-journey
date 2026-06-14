from decimal import Decimal
print("1==>jam")
print("2==>tafrigh")
print("3==>zarb")
print("4==>taghsim")
print("5==>khorooj")
print("amal mohasebatie entekhabira vared konid:")
amal_e_mohasebati = int(input())
while amal_e_mohasebati > 5:
    amal_e_mohasebati = int(input())
while amal_e_mohasebati < 5:
    if amal_e_mohasebati == 1:
        addad_1 = Decimal(input("adad aval ra vared konid:"))
        addad_2 = Decimal(input("adad dovvom ra vared konid:"))
        print(f"natije:{addad_1 + addad_2}")
        print("amale jadid ra vared konid:")
        amal_e_mohasebati = int(input())
    elif amal_e_mohasebati == 2:
        addad_1 = Decimal(input("adad aval ra vared konid:"))
        addad_2 = Decimal(input("adad dovvom ra vared konid:"))
        print(f"natije:{addad_1 - addad_2}")
        print("amale jadid ra vared konid:")
        amal_e_mohasebati = int(input())
    elif amal_e_mohasebati == 3:
        addad_1 = Decimal(input("adad aval ra vared konid:"))
        addad_2 = Decimal(input("adad dovvom ra vared konid:"))
        print(f"natije:{addad_1 * addad_2}")
        print("amale jadid ra vared konid:")
        amal_e_mohasebati = int(input())
    elif amal_e_mohasebati == 4:
        addad_1 = Decimal(input("adad aval ra vared konid:"))
        addad_2 = Decimal(input("adad dovvom ra vared konid:"))
        print(f"natije:{addad_1 / addad_2}")
        print("amale jadid ra vared konid:")
        amal_e_mohasebati = int(input())
print("khodahafez")