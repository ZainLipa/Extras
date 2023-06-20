import sympy as sp

def symbolic_derivative(expression, variable):
    expr = sp.sympify(expression)
    derivative = sp.diff(expr, variable)
    return derivative

# Example usage
expression = input("Enter a mathematical expression: ")
variable = input("Enter the variable with respect to which you want to differentiate: ")

derivative = symbolic_derivative(expression, variable)
print("Derivative:", derivative)
