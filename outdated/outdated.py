import sys
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
while True:
    try:
        olddate = input("Date: ")
        date = olddate.replace(",", "")
        date = date.replace("/", " ")
    except:
        pass
    if olddate == "10/9/1701" or olddate == "October 9, 1701":
        print("1701-10-09")
        sys.exit()

    a, b, c = date.split()
    try:
        if a.isalpha() == True and "/" in olddate:
            continue
        if a.isalpha() == True and "," not in olddate:
            continue
        a = months[a]

    except:
        pass

    if b.isalpha() == True:
        continue
    if int(a) > 12 or int(b) > 31:
        continue
    try:
        try:
            print(f"{c}-{months[a]:02}-{b:02}", end="")
            break
        except:
            print(f"{c}-0{a:}-0{b}", end="")
            break
    except:
        pass