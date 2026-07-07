import math

print("========== SCIENTIFIC CALCULATOR ==========")

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power (x^y)")
print("6. Square (x²)")
print("7. Square Root (√x)")
print("8. Cube (x³)")
print("9. Cube Root (∛x)")
print("10. Sine (sin)")
print("11. Cosine (cos)")
print("12. Tangent (tan)")
print("13. Log Base 10")
print("14. Natural Log (ln)")
print("15. Factorial")
print("16. Exit")
print()
print()
print("choose the number")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    print("Result =", a + b)

elif choice == 2:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    print("Result =", a - b)

elif choice == 3:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    print("Result =", a * b)

elif choice == 4:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero.")

elif choice == 5:
    a = float(input("Enter Base Number: "))
    b = float(input("Enter Power: "))
    print("Result =", a ** b)

elif choice == 6:
    a = float(input("Enter Number: "))
    print("Square =", a ** 2)

elif choice == 7:
    a = float(input("Enter Number: "))
    print("Square Root =", math.sqrt(a))

elif choice == 8:
    a = float(input("Enter Number: "))
    print("Cube =", a ** 3)

elif choice == 9:
    a = float(input("Enter Number: "))
    print("Cube Root =", a ** (1/3))

elif choice == 10:
    a = float(input("Enter Angle in Degrees: "))
    print("Sin =", math.sin(math.radians(a)))

elif choice == 11:
    a = float(input("Enter Angle in Degrees: "))
    print("Cos =", math.cos(math.radians(a)))

elif choice == 12:
    a = float(input("Enter Angle in Degrees: "))
    print("Tan =", math.tan(math.radians(a)))

elif choice == 13:
    a = float(input("Enter Number: "))
    print("Log =", math.log10(a))

elif choice == 14:
    a = float(input("Enter Number: "))
    print("Natural Log =", math.log(a))

elif choice == 15:
    a = int(input("Enter Number: "))
    print("Factorial =", math.factorial(a))

elif choice == 16:
    print("Calculator Closed.")

else:
    print("Invalid Choice")