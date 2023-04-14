import sys

from pyfiglet import Figlet

if len(sys.argv) == 2:
    sys.exit("Wrong usage.")
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":

        try:
            font = Figlet(font=f"{sys.argv[2]}")
        except:
            sys.exit("Wrong Usage.")

        text = input("Input: ")
        print("Output: ", end="")


        print(font.renderText(text))

    else:
        sys.exit("Wrong usage.")

else:
    text = input("Input: ")
    print("Output: ", end="")

    font = Figlet(font='slant')
    print(font.renderText(text))
