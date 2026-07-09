class Animal:
    def eat(self):
        print("Animal marks a sound")
class Dog(Animal):
    def bark(self):
        print("Dog   walks")
class cat(Animal):
    def meow(self):
        print("cat sound the  meow")
class pig(Animal):
    def ooh(self):
        print("pig is sitting in  the floor")
class ant(Animal):
    def goline(self):
        print("ant goes in a line")
dog1 =Dog()
dog1.eat()
dog1.bark()
meow = cat()
meow.eat()
meow.meow()
ooh =pig()
ooh.eat()
ooh.ooh()
goline =ant()
goline.eat()
goline.goline()