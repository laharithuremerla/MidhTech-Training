from abc import ABC,abstractmethod
class Vehicle(ABC):
   @abstractmethod
   def start(self):
      pass
   
class Car(Vehicle):
   def start(self):
      print("car start with a key")
car1= Car()
car1.start()