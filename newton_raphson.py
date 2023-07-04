# Program of the Day: Newton-Raphson Method for Finding Roots

def newton_raphson(function, derivative, initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess

    for i in range(max_iterations):
        fx = function(x)
        if abs(fx) < tolerance:
            break

        dfx = derivative(x)
        if dfx == 0:
            break

        x = x - fx / dfx

    return x

# Example usage
def function(x):
    return x**3 - 2*x - 5

def derivative(x):
    return 3*x**2 - 2

root = newton_raphson(function, derivative, initial_guess=2)
print("Approximate root:", root)

