class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.__marks = marks

    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.__marks)

        if self.__marks >= 35:
            print("Result : Pass")
        else:
            print("Result : Fail")


student1 = Student("Lahari", 21, 75)
student1.display()