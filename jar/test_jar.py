from jar import Jar

def test_init():
     jar = Jar(1)
     assert jar.capacity == 1
     assert jar.size == 0

     jar = Jar(5)
     assert jar.capacity == 5
     assert jar.size == 0

     jar = Jar()
     assert jar.capacity == 12
     assert jar.size == 0

def test_str():
     jar = Jar()
     assert str(jar) == ""
     jar.deposit(1)
     assert str(jar) == "🍪"
     jar.deposit(5)
     assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
     jar = Jar()
     jar.deposit(2)
     assert jar.size == 2
     jar.deposit(5)
     assert jar.size == 7

def test_withdraw():
     jar = Jar()
     jar.deposit(12)
     jar.withdraw(2)
     assert jar.size == 10
     jar.withdraw(7)
     assert jar.size == 3