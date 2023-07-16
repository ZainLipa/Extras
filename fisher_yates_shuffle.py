# Program of the Day: Fisher-Yates Shuffle

import random

def fisher_yates_shuffle(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

    return arr

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_array = fisher_yates_shuffle(array)
print("Shuffled array:", shuffled_array)
