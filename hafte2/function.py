from decimal import Decimal
ayar = int(input("ayar tala ro vared konid:"))
vazn = Decimal(input("vazn ra vared konid:"))
gheimate_tala = Decimal(input("gheimate tala ra vared konid:"))
def gheimat(ayar, vazn, gheimat):
    return (ayar * vazn / 750) * gheimat
gheimate_nahae = gheimat(ayar, vazn, gheimate_tala)
print(
    f"gheimate tala: {gheimate_tala}",
    f"vazne tala: {vazn}",
    f"ayare tala: {ayar}",
    f"mablagh: {gheimate_nahae}",
    sep="\n"
)