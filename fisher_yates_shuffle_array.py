# Program of the Day: Fisher-Yates Shuffle Algorithm (Array Shuffling)

import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

# Example usage
original_array = [1, 2, 3, 4, 5]
shuffled_array = original_array.copy()
fisher_yates_shuffle(shuffled_array)

print("Original Array:", original_array)
print("Shuffled Array:", shuffled_array)
