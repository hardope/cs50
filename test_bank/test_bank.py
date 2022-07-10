from bank import value

def test_value():
     assert value("Hello what's up") == 0
def test_value2():
     assert value('Hey how are you') == 20
def test_value3():
     assert value('Good day how are you doing') == 100