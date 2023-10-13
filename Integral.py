#Potd integral
from scipy.integrate import quad

# Define the function to be integrated
def integrand(x):
    return x**2

# Define the limits of integration
a = 0
b = 1

# Call the quad function to perform the integration
result, error = quad(integrand, a, b)

# Print the result
print(f"The integral of x^2 from {a} to {b} is {result:.3f}")
