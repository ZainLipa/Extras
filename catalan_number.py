# Program of the Day: Catalan Number Calculator (Dynamic Programming)

def catalan_number(n):
    if n == 0:
        return 1

    catalan = [0] * (n + 1)
    catalan[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan[n]

# Example usage
n = 5
result = catalan_number(n)
print(f"The {n}-th Catalan number is:", result)
