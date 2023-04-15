import os
from pyfiglet import Figlet

def font(text):
    text = Figlet (font="slant")
    os.system("cls")
    os.system( 'mode con: cols-75 lines-30')

    return str(text.renderText(text))

print (font("Jeremiah"))
