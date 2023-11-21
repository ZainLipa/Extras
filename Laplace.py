#Program of the day: LAPLACE
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        submatrix = [[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += (-1) ** j * matrix[0][j] * determinant(submatrix)

    return det

# Example matrix for demonstration
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

det = determinant(matrix)

print("Determinant: ", det)
