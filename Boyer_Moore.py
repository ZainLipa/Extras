# Program of the Day: Boyer-Moore Majority Vote Algorithm
def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Validation step to check if the candidate is the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > len(nums) // 2:
        return candidate
    else:
        return None

# Example usage
nums = [3, 1, 7, 1, 1, 7, 1, 7, 7]
result = majority_element(nums)
if result is not None:
    print("Majority element:", result)
else:
    print("No majority element found.")
