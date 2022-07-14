def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = str(d)
    d = d.replace("$", "")
    d = float(d)
    return d
    # TODO


def percent_to_float(p):
    # TODO
    p = str(p)
    p = p.replace("%", "")
    p = float(p)
    p = p/100
    return p


main()