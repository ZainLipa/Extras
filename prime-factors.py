def find_prime_factors(num):
    factors = []
    divisor = 2

    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1

    return factors

number = int(input("Enter a number: "))

prime_factors = find_prime_factors(number)

print("Prime factors of", number, "are:", prime_factors)
