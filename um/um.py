import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
     a = 0
     if s == 'um':
          a = 1
     list = re.findall(r"\b\W*um\W", s.lower())
     return len(list) + a

if __name__ == "__main__":
    main()