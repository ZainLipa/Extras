import math

def calculate_triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

triangle_area = calculate_triangle_area(side_a, side_b, side_c)

print("The area of the triangle is:", triangle_area)
