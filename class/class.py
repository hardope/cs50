class Wizard:
     def __init__(self, name):
          if not name:
               raise ValueError("Missing name")
          self.name = name

class Student:
     def __init__(Wizard):
          super ().__init__(name)
          self.house = house
     def __str__(self):
          return f"{self.name} is from {self.house}"

class Professor:
     def __init__(self, name, subject):
          self.subject = subject
     def __str__(self):
          return f"{self.name} teaches {self.subject}"

wizard = Wizard('Albus')
print(Student('James'))
print(Professor('Harry'))