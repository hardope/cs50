while True:
    fraction = input("Fraction: ")
    try:
        int(fraction[0])
        int(fraction[2])

        if int(fraction[2]) == 0 or fraction[1] != "/":
            pass
        elif "." in fraction:
            pass
        elif fraction[0] > fraction[2]:
            pass
        else:
            break

    except:
        pass

a = fraction[0]
b = fraction[2]

try:
    percent = (float(a) / float(b)) * 100
    if percent > 99.0:
        print("F", end="")
    elif percent < 1.0:
        print("E", end="")
    else:
        print(f"{int(percent)}%", end="")
except:
    pass
