# create derivative function
def derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example usage
def f(x):
    return x**2  # Define your function here

x = 2  # Point at which to approximate the derivative
h = 0.001  # Step size

approx_derivative = derivative(f, x, h)
print("Approximate Derivative:", approx_derivative)
