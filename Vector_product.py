#potd dot product
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    result = sum(x * y for x, y in zip(vector1, vector2))
    return result

# Example vectors for demonstration
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

dot_product_result = dot_product(vector1, vector2)

print("Dot Product Result:", dot_product_result)
