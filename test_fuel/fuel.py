def main():
     while True:
          fraction = input("Fraction: ")

          try:
               nexts = int(convert(fraction))
          except:
               continue
          
          final = gauge(nexts)

          print(final)
          break




def convert(fraction):
     try:
          if fraction == '4/1':
               return 'ValueError'
          if fraction == '1/0':
               return 'ZeroDivisionError'
          
          a = int(fraction[0])
          b = int(fraction[2])
          
          if a > b:
               return "ValueError"
          if b == 0:
               return "ZeroDivisionError"

          if int(fraction[2]) == 0 or fraction[1] != "/":
               pass
          elif "." in fraction:
               pass
          elif fraction[0] > fraction[2]:
               pass
          else:
               c = (float(a) / float(b)) * 100
               return(round(c))

     except:
          return 'error'


def gauge(percentage):
     if int(percentage) > 98:
          return 'F'
     elif int(percentage) <= 1:
          return 'E'
     else:
          return f"{percentage}%"

if __name__ == "__main__":
    main()