def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

number_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input numbers to integers
numbers = [int(num) for num in number_list]

maximum = find_maximum(numbers)

if maximum is not None:
    print("The maximum number is:", maximum)
else:
    print("No numbers were provided.")
