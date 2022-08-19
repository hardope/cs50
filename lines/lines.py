import sys

#this is a comment

if len(sys.argv) > 2:
     sys.exit("Too many command line arguments.")
elif len(sys.argv) < 2:
     sys.exit("Too few command line arguments.")


file_name = sys.argv[1]
a = len(file_name) - 1

if file_name[a] != 'y' and file_name[a - 1] != 'p' and file_name[a-2] != '.':
     sys.exit("Not a python file.")
else:
     pass

try:
     with open(sys.argv[1]) as file:
          count = 0
          for line in file:
               if not line.lstrip().startswith('#') and line.lstrip() != "":
                    count+=1
     print(count)
except:
     sys.exit("File does not exit.")
