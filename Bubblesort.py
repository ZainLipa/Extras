def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Example usage:
numbers = [5, 2, 8, 12, 1, 9]
print("Original list:", numbers)
bubble_sort(numbers)
print("Sorted list:", numbers)
