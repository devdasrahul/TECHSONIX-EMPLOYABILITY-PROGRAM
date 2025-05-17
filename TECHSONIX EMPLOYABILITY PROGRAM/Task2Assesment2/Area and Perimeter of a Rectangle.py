# This script calculates the area and perimeter of a rectangle based on user input.

# Take length and width input from the user and convert to float
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
