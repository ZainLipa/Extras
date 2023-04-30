# Define the arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Take user input
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform the calculation
if op == '+':
    print(num1, "+", num2, "=", add(num1, num2))

elif op == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif op == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif op == '/':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid operator")
