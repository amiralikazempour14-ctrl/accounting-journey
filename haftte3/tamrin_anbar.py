from decimal import Decimal
class Moshtari:
    def __init__(self, name, mande):
        self.name = name
        self.mande = mande
    def __str__(self):
        return f"nam: {self.name} - mande: {self.mande}"


class Hesab:
    def __init__(self, moshtari):
        self.moshtari = moshtari
        self.history_receive = []
        self.history_send = []
    def receive(self, mablagh):
        self.moshtari.mande += mablagh
        self.history_receive.append(mablagh)
    
    def send(self, mablagh):
        if self.moshtari.mande > mablagh:
            self.moshtari.mande -= mablagh
            self.history_send.append(mablagh)
        else:
            print("mablagh kharj shode bishtar az mojuudi ast")
    def receive_history(self):
            for trans in self.history_receive:
                print(f"tarikhcheye daryaft: {trans}")
    def send_history(self):
        for trans in self.history_send:
            print(f"tarikhcheye pardakht:{trans}")

a = Moshtari("amirali", Decimal("20000000000"))
b = Hesab(a)
b.receive(Decimal("7000000000"))
b.receive(Decimal("50000000000"))        
b.send(Decimal("5000000000"))
print(a)
print(b.history_receive, b.history_send)

