def is_year_leap (year):
        if year % 4 == 0:
            result = year
            print(True)
            return result
        else:
            result_2 = year
            print(False)
            return result_2
x = is_year_leap (2000)
print(x)
