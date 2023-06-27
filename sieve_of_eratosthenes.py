# Program of the Day: Sieve of Eratosthenes

def sieve_of_eratosthenes(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    primes = [num for num, is_prime in enumerate(prime) if is_prime]
    return primes

# Example usage
limit = int(input("Enter the upper limit: "))

prime_numbers = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, "are:", prime_numbers)
