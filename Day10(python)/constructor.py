class Student:  
  def __init__(self,name,age):
        self.name =name
        self.age = age
  def display(self):
      print("name:",self.name)
      print("Age :",self.age)
s1= Student("lahari",20)
s1.display()