
class Mailing:


    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = int(cost)
        self.track = str(track)

    def ToAdd(self, to_address):
        self.to_address = to_address

    def GetToAdd(self):
        return self.to_address

    def FromAdd(self, from_address):
        self.from_address = from_address

    def GetFromAdd(self):
        return self.from_address

    def res(self):
        print(f"Отправление ", str(self.track),  "из", str(self.from_address), " в ", str(self.to_address), "Стоимость", str(self.cost), "рублей")

