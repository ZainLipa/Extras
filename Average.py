def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Prompt the user to enter list of numbers separated by spaces
number_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input numbers to integers
numbers = [int(num) for num in number_list]

# Calculate the average of the numbers
average = calculate_average(numbers)

print("Average :", average)
