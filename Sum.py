def sum_even_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The sum of the even numbers in the list", numbers, "is", sum_even_numbers(numbers))
