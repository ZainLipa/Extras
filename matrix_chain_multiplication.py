# Program of the Day: Matrix Chain Multiplication (Dynamic Programming)

import sys

def matrix_chain_multiplication(dims):
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]

# Example usage
dimensions = [10, 30, 5, 60]
minimum_cost = matrix_chain_multiplication(dimensions)
print("Minimum cost of matrix chain multiplication:", minimum_cost)
