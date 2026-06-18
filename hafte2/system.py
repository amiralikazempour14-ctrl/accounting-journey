from decimal import Decimal
anbar = []
def add_kala(anbar):
    khorooj = 2
    while khorooj != 1:
        try:
            price = Decimal(input("price kala ra vared konid:"))
            vazn = Decimal(input("vazn kala ra vared konid:"))
            ayar = Decimal(int(input("ayar kala ra vared konid:")))
            anbar.append({"price": price, "vazn": vazn, "ayar": ayar})
            khorooj = int(input("khorooj ra vared konid:1==>yes, 2==>no"))
        except:
            print("voroodi shoma ghalat ast dobare emtehan konid")
def show_anbar(anbar):
    for kala in anbar:
        print(f"price: {kala['price']}, vazn: {kala['vazn']}, ayar: {kala['ayar']}")
def value_anbar(anbar):
    value = [kala["price"] * kala["vazn"] * kala["ayar"] / 750 for kala in anbar]
    jam = sum(value).quantize(Decimal("0.01"))
    print(f"value anbar: {jam}")
while True:
    print("1==>add kala")
    print("2==>show anbar")
    print("3==>value anbar")
    print("4==>exit")
    choice = int(input("choice ra vared konid:"))
    if choice == 1:
        add_kala(anbar)
    elif choice == 2:
        show_anbar(anbar)
    elif choice == 3:
        value_anbar(anbar)
    elif choice == 4:
        break