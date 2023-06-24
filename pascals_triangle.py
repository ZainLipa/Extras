# Program of the Day: Pascal's Triangle

def generate_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

# Example usage
num_rows = int(input("Enter the number of rows: "))

pascals_triangle = generate_pascals_triangle(num_rows)
print("Pascal's Triangle:")
for row in pascals_triangle:
    print(row)
