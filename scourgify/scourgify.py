import csv
import sys

data = []

if len(sys.argv) > 3:
     sys.exit("Too many command line arguments.")
elif len(sys.argv) < 3:
     sys.exit("Too few command line arguments.")

try:
     with open(sys.argv[1]) as file:
          pass
except:
     sys.exit(f"could not read {sys.argv[1]}")


if sys.argv[1][-4:] == '.csv' or sys.argv[1][-4:] == '.csv':
     try:
          with open(sys.argv[1]) as file:
               reader = csv.DictReader(file)
               for read in reader:
                    data.append(read)

          out = open(sys.argv[2], 'w', newline="")
          writer = csv.DictWriter(out, fieldnames=['first', 'last', 'house'])
          writer.writeheader()
          out.close()

          with open(sys.argv[2], 'a', newline="") as file:
               writer = csv.writer(file)
        

               for i in data:
                    print(i)
                    last, first = i['name'].split(',')
                    first=first.strip()
                    last = last.strip()
                    house = i['house'].strip()

     
                    writer.writerow({first : first, last: last, house: house})
     except:
          sys.exit("File does not exit.")
else:
    sys.exit("Not a CSV file")