def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_primes(start, end):
    prime_sum = 0
    for num in range(start, end+1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total_sum = sum_primes(start, end)

print("The sum of prime numbers between", start, "and", end, "is:", total_sum)
