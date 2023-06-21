def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n+1)]
    y = [f(xi) for xi in x]

    integral = y[0] + y[-1]
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * y[i]
        else:
            integral += 4 * y[i]
    
    integral *= h / 3
    return integral

# Example usage
def f(x):
    return x**2  # Define your function here

a = 0  # Lower limit of integration
b = 1  # Upper limit of integration
n = 4  # Number of intervals (must be even)

integral = simpsons_rule(f, a, b, n)
print("Area under the Curve:", integral)
