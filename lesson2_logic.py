user_login = "adam"
user_password = "123qwe"
login = input("Логин: ")
password = input("Пароль: ")
if login == user_login and password == user_password:
    print("Ура!")
else: print("Некорректные данные")


crit = "red"
crit_1 = "lock"

color = input("Цвет: ")
feature = input("Фичи: ")
if color == crit or feature == crit_1:
    print("такая сумка есть в наличии")
else: print("Нет в наличии")