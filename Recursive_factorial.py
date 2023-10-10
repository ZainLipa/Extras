#Program of the day: Recursive Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Error: Please enter a non-negative integer.")
else:
    fact = factorial(num)
    print("The factorial of", num, "is", fact)
