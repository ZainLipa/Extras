def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        digit = binary % 10
        decimal += digit * (2 ** power)
        binary //= 10
        power += 1
    return decimal

binary_num = int(input("Enter a binary number: "))

decimal_num = binary_to_decimal(binary_num)

print("Decimal equivalent:", decimal_num)
