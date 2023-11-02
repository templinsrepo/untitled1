def bank(x,y):
    for i in range(y):
        x = x + (x/100*10)
        print(x)

bank(5000, 3)