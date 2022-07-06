from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for i in range(n):
    # central for loop
    for b in range(n - i - 1):
        # loop for space
        print(" ", end="")
    for j in range(i + 1):
        # loop for first set of Hashes
        print("#", end="")
    print("  ", end="")
    # prints Central space
    for k in range(i + 1):
        # loop for last set of Hashes
        print("#", end="")
    print("")