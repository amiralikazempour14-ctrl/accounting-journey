from decimal import Decimal
gheymatha = [Decimal("15000") , Decimal("35000") , Decimal("23500")]
bishtaringheimat = Decimal("0")
for gheimat in gheymatha:
    if gheimat > bishtaringheimat:
        bishtaringheimat = gheimat
print(f"geran tarin kala:{bishtaringheimat}")