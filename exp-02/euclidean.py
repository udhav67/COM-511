import math

# Function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Example usage
x1, y1 = 1, 2  # Coordinates of the first point
x2, y2 = 4, 6  # Coordinates of the second point

distance = euclidean_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")
