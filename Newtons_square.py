# Program of the Day: Newton's Method for Finding Square Roots

def newton_square_root(n, tolerance=0.0001):
    guess = n / 2
    while abs(guess * guess - n) > tolerance:
        guess = (guess + n / guess) / 2
    return guess

# Example usage
number = float(input("Enter a number: "))

result = newton_square_root(number)
print("Square root of", number, "is:", result)
