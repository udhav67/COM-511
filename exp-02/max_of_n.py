# Input the value of n
n = int(input("Enter the number of values to compare: "))

# Initialize the maximum to negative infinity
max_value = float('-inf')

# Loop to input and compare n values
for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    if value > max_value:
        max_value = value

# Print the maximum value
print(f"The maximum value among the {n} numbers is: {max_value}")
