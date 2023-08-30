# Program of the Day: Fast Exponentiation (Power Modulo)

def fast_exponentiation(base, exponent, modulo):
    result = 1
    base %= modulo

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulo
        exponent //= 2
        base = (base * base) % modulo

    return result

# Example usage
base = 5
exponent = 13
modulo = 1000000007

result = fast_exponentiation(base, exponent, modulo)
print(f"{base}^{exponent} % {modulo} =", result)
