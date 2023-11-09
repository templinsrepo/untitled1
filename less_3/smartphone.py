class Smartphone:

    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

phone = Smartphone("Iphone", "14", "+79999999999")
print(phone.brand + " - " + phone.model + " - " + phone.phone_number )
