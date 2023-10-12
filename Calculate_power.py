#POTD power calculator
def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

power = calculate_power(base, exponent)

print(base, "raised to the power of", exponent, "is:", power)
