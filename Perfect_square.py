#Perfect Square
def is_perfect_square(num):
    square_root = int(num ** 0.5)
    return square_root * square_root == num

num = int(input("Enter a positive integer: "))

if is_perfect_square(num):
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")
