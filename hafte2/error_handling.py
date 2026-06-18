from decimal import Decimal
while True:
    try:
        vazn = Decimal(input("lotfan vazne tala ra vared konid:"))
        print(f"vazne vared shode={vazn}gr")
        break
    except:
        print("voroodi shoma ghalat ast dobare emtehan konid")
while True:
    try:
        gheimat = Decimal(input("lotfan gheimat ra vared konid:"))
        print(f"gheimat vared shode={gheimat}")
        break
    except:
        print("voroodi shoma ghalat ast dobare emtehan konid")
while True:
    try:
        ayar = Decimal(input("lotfan ayar ra vared konid:"))
        print(f"ayar vared shode={ayar}")
        break
    except:
        print("voroodi shoma ghalat ast dobare emtehan konid")
mablaghe_tala = gheimat*vazn/750*ayar
print("mablagh tala shoma:",mablaghe_tala.quantize(Decimal("0.01")))