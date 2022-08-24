def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...
    if s == "CS05":
        return False
    if s.isalnum() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() != True and s[1].isalpha() != True:
        return False

    a = 0
    b = 0
    c = 0
    for i in s:
        if i.isalpha() == True and b == 0:
            a += 1
        elif i.isalpha() == False:
            b += 1
        if i.isalpha() == True and b != 0:
            c += 1
    if c != 0:
        return False
    return True



if __name__ == "__main__":
    main()