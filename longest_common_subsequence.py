# Program of the Day: Longest Common Subsequence

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a matrix to store the lengths of common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Retrieve the longest common subsequence
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Example usage
string1 = "AGGTAB"
string2 = "GXTXAYB"
lcs = longest_common_subsequence(string1, string2)
print("Longest Common Subsequence:", lcs)
