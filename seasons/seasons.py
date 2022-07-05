from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():
     dob = input("Date of birth: ")
     try:
          year, month, day = check_date(dob)
     except:
          sys.exit("Invalid date")
     new_dob = date(int(year), int(month), int(day))
     today = date.today()
     difference = today - new_dob
     minutes = difference.days * 24 * 60
     out = p.number_to_words(int(minutes), andword="")
     print(out.capitalize() + " minutes")

def check_date(date):
     if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", date):
          year, month, day = date.split("-")
          return year, month, day


if __name__ == "__main__":
    main()