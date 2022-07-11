from fuel import gauge, convert
import sys

def test_gauge():
     assert gauge(10) == '10%'
     assert gauge(45) == '45%'
     assert gauge(1) == 'E'
     assert gauge(99) == 'F'
     
     
def test_convert():
     assert convert('1/2') == 50
     assert convert('3/4') == 75
     assert convert('3/4') == 75
     assert convert('1/0') == 'ZeroDivisionError'
     assert convert('4/0') == 'ValueError'
     
