# Program of the Day: Longest Increasing Subsequence

def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    return max_length

# Example usage
sequence = [10, 22, 9, 33, 21, 50, 41, 60]
length = longest_increasing_subsequence(sequence)
print("Length of the longest increasing subsequence:", length)
