def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print()

print("Arithmetic Operations")
print("Addition =", addition(num1, num2))
print("Subtraction =", subtraction(num1, num2))
print("Multiplication =", multiplication(num1, num2))
print("Division =", division(num1, num2))