import math

# Function to calculate area and perimeter of a circle
def circle_area_and_perimeter(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Function to calculate area and perimeter of a square
def square_area_and_perimeter(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter

# Function to calculate area and perimeter of a rectangle
def rectangle_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Input choice of shape from the user
print("Select a shape:")
print("1. Circle")
print("2. Square")
print("3. Rectangle")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area, perimeter = circle_area_and_perimeter(radius)
    print(f"Area of the circle: {area}")
    print(f"Perimeter of the circle: {perimeter}")
elif choice == 2:
    side_length = float(input("Enter the side length of the square: "))
    area, perimeter = square_area_and_perimeter(side_length)
    print(f"Area of the square: {area}")
    print(f"Perimeter of the square: {perimeter}")
elif choice == 3:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area, perimeter = rectangle_area_and_perimeter(length, width)
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")
else:
    print("Invalid choice. Please select 1, 2, or 3 for circle, square, or rectangle.")
