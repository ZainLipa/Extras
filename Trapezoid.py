def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2

    for i in range(1, n):
        x = a + i * h
        integral += f(x)

    integral *= h
    return integral

# Example usage
def f(x):
    return x**2  # Define your function here

a = 0  # Lower limit of integration
b = 1  # Upper limit of integration
n = 100  # Number of intervals

integral = trapezoidal_rule(f, a, b, n)
print("Definite Integral:", integral)
