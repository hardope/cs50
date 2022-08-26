import requests
import json
import sys
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

amount = 0

def intWithCommas(x):
    if type(x) not in [type(0), type(0)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

if len(sys.argv) < 2:
     sys.exit("Missing commannd line arguement.")
elif len(sys.argv) > 2:
     sys.exit("Too many command line arguments.")
else:
     try:
          amount = float(sys.argv[1])
     except:
          sys.exit("Command line arguement is not a number.")
     try:
          responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
          object = responce.json()

          price = object['bpi']['USD']['rate']
          price = price.replace(",", "")
          price = float(price) * amount
          price = str(price)
          
          a, b = price.split('.')
          a = int(a)

          print(f"{intWithCommas(a)}.{b}")

          
          #price = float(price) * float(sys.argv[1]) 
     except:
          sys.exit("Something went wrong, Try again.")
     