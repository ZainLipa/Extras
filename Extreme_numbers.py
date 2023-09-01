#POTD Find extremes
def find_extremes(numbers):
    if len(numbers) == 0:
        return None, None
    smallest = largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

number_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input numbers to integers
numbers = [int(num) for num in number_list]

smallest, largest = find_extremes(numbers)

if smallest is not None and largest is not None:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were provided.")
