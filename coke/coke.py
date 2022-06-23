value = 50
while value >= 1:
    coin = int(input("Insert coin: "))
    if coin != 30:
        value = value - coin



    if value > 0:
        print(f"Amount due: {value}")

    elif value <= 0:
        print(f"Change Owed: {-1 * value}")
