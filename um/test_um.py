from um import count

def test_case():
     assert count('um') == 1
     assert count('um,') == 1
     assert count('UM,') == 1
def test_case1():
     assert count('um, hello') == 1
     assert count('um, hello plum') == 1

def test_case2():
     assert count('plum album hello um, um.') == 2
     assert count('plum album hello um,') == 1

def test_noum():
     assert count('Can you believe this umbrella is blue') == 0
     assert count('Can you believe this.') == 0