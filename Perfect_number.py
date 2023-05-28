def is_perfect_number(num):
    if num <= 0:
        return False
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return num == divisor_sum

num = int(input("Enter a positive integer: "))

if is_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
