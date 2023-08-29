#Program of the day, GCD
def gcd(a, b):
    """
    Calculates the greatest common divisor (gcd) of two integers using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

print(gcd(5,4))
