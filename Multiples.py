#POTD multiples
def calculate_multiples_sum(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

number = int(input("Enter a number: "))

sum_of_multiples = calculate_multiples_sum(number)

print("Sum of multiples of 3 or 5 below", number, "is:", sum_of_multiples)
