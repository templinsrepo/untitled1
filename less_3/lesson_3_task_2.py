from smartphone import Smartphone
catalog = []
brands = ['iphone', 'samsung', 'lg', 'xiaomi', 'honor']
models = ['14', '40', '34', '12 Pro', '80 lite']
phone_number = ['+79031111111', '+79032222222', '+79033333333', '+79034444444', '+79035555555']

for brand, model, number in zip(brands, models, phone_number):
    for_input = Smartphone(brand, model, number)
    print(f'{for_input.brand} - {for_input.model} - {for_input.phone_number}')