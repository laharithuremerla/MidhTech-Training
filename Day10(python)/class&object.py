class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        
        if(self.marks >= 35 ):
            result= "pass"
        else: 
             result ="Fail"

        print("Name :", self.name)
        print("Age :", self.age)
        print("Marks :", self.marks)
        print("Result :", result)


student1 = Student("Lahari", 21, 22)
student1.display()