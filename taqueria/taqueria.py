stock = {
    "Baja Taco": 4.000,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0.00
while True:
    try:
        line = input("Item: ")
        try:
            price = price + stock[line.title()]
            converted = "{:.2f}".format(price)
            print(f"Total: ${converted}")
        except:
            pass


    except:
        break