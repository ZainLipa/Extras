# Program of the day Linear Equations
import numpy as np

def solve_linear_equations(coefficients, constants):
    A = np.array(coefficients)
    b = np.array(constants)
    
    try:
        solution = np.linalg.solve(A, b)
        return solution.tolist()
    except np.linalg.LinAlgError:
        return None

# Example usage
coefficients = [[2, 1, -1], [1, -
