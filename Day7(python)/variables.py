student_name = "Lahari"
studentName = "Lahari"
StudentName = "Lahari "

print("snake_case :", student_name)
print("camelCase  :", studentName)
print("PascalCase :", StudentName)


print()

age= 20
print("basic  example :", age)
student = "Lahari"
Course = "Python"
paid_student = 15
print("studentName:", student)
print("Course:", Course)
total_amount_per_student =100
total_paid_students = 15*total_amount_per_student
print("total_paid_students:", total_paid_students)


print()

name = "Lahari"
age = 20
mail = "lahari200422@gmail.com"
clg_name="GIST"
print(f"My name is {name} and my age is {age}. My mail id is {mail} and I am studying in {clg_name}.")


print()

user_name = "Lahari"
logged_in = False
if(logged_in):
    print(f"Welcome {user_name}!")
else:
    print("Please log in to continue.")

print()
Student_name = "Lahari"
age = 20
is_logged_in = True
marks=19.8
percentage= 95.8
print("age:", age, "type:", type(age))
print("is_logged_in:", is_logged_in, "type:", type(is_logged_in))
print("Student_name:", Student_name, "type:", type(Student_name))
print("marks:", marks, "type:", type(marks))
print("percentage:", percentage, "type:", type(percentage))

print()
type_casting =20

a= True
b= False
print(int(a))
print(int(b))
age= 10
marks=0
print(bool(age))
print(bool(marks))


print()

# name=  str(input("Enter your name: "))
# age=  int(input("Enter your age: "))
# marks= float(input("Enter your marks: "))
# print()

# length  = int(input("Enter the length of rectangle: "))
# width  = int(input("Enter the width of rectangle: "))
# area = length * width
# print(f"The area of rectangle is: {area}")

print()

telugu=100
hindi=90
english=80
maths=70
science=60
social=50
total_marks= telugu+hindi+english+maths+science+social
percentage= (total_marks/600)*100
print(f"The total marks of student is: {total_marks}")
print(f"The percentage of student is: {percentage}")

print()

wallet_balance= 1000
wallet_balance -= 500
wallet_balance += 200
print("your current wallet balance is:", wallet_balance)
print()
My_wallet_balance= 1000
My_friend_wallet_balance= 500
if(My_friend_wallet_balance==My_wallet_balance):
    print("True")
else:
    print("False")

print()


age= 20
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


print()
   

attendance= 90
fee_paid= True
if(attendance>=75 and fee_paid==True):
    print("You are eligible to appear for the exam.")

print()

basket= ["apple", "banana", "orange", "grapes"]
basket2 =["mango", "kiwi", "watermelon, apple"]
card = basket + basket2
unique_card = set(card)
print("The unique card contains:", unique_card)

if("apple" in card):
    print("Yes, apple is present in the card.")

print()
Card = ["apple", "banana", "orange", "grapes"]
smart_card = Card
new_card = ["apple", "banana", "orange", "grapes"]
print("The smart card contains:", Card)
print("The new card contains:", Card)


print()

READ = 1
WRITE =2
EXCUTE =4
user_permission =READ | WRITE
print("can read:" ,bool(user_permission & READ))
print("can write:" ,bool(user_permission & WRITE))
print("can excute:" ,bool(user_permission & EXCUTE))

print()

val1 =20
val2 = 10
val3= 30

max_result= max(val1, val2, val3)
min_result= min(val1, val2, val3)
print("Maximum value:", max_result)
print("Minimum value:", min_result)
 
print()
val1 = 20
val2 = 10
val3 = 70
if(val1>val2 and val1>val3):
    print("val1 is maximum")
elif(val2>val1 and val2>val3):
    print("val2 is maximum")
elif(val3>val1 and val3>val2):
    print("val3 is maximum")
elif(val1==val2 and val1==val3):
    print("All values are equal")
elif(val1==val2 and val1>val3):
    print("val1 and val2 are equal and greater than val3")
else:
    print("val1 and val3 are equal and greater than val2")
if(val1<val2 and val1<val3):
    print("val1 is minimum")
elif(val2<val1 and val2<val3):
    print("val2 is minimum")
else:
    print("val3 is minimum")
   


# marks=int(input("Enter your marks: "))
# if(marks>=90):
#     print("grade = A")
# elif(marks>=80):
#     print("grade = B")
# elif(marks>=60):
#     print("grade = c")
# else:
#      print("Has to improve")



print()

# age = int(input("enter your age: "))
# citizen = True
# if(age>=18):
#     if citizen:
#         print("allowed to vote")
#     else:
#        print("not allowed to vote" )
# else:
#     print("age must not be less than 18")
  
# operated = input("select the operated : +,-,*,/")
# num1 = int(input("enter  your num1 :"))
# num2 = int(input("enter  your num2: "))
# if(operated =="+"):
#    result =num1+num2
#    print(result)
# elif(operated =="-"):
#     result =num1-num2
#     print(result)
# elif(operated =="/"):
#     result =num1/num2
#     print(result)
# elif(operated =="*"):
#     result =num1*num2
#     print(result)
# else:
#     print("operater is not in the requiment")
print()

count  =6
while count>=5:
    print("basic example:",count)
    count-=1
print(count)

  

print()

count = 1
while count<=5:
    if(count == 3):
        continue
    count+=1;   
print(count)
