# Program of the Day: Binary Search Algorithm

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

index = binary_search(sorted_array, target)
if index != -1:
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found in the array")
