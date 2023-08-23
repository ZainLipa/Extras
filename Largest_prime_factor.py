#Program of the day Largest Prime Factor 
def largest_prime_factor(number):
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
        else:
            factor += 1
    if number > 1:
        return number
    return factor

# Example usage
number = int(input("Enter a number: "))
largest_prime = largest_prime_factor(number)
print("Largest Prime Factor:", largest_prime)
