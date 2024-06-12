import math
# Define the dimensions of the rectangle
rectangle_width = 16.5  # in meters
rectangle_length = 31  # in meters

# Calculate the area and circumference of the rectangle
rectangle_area = rectangle_width * rectangle_length
rectangle_circumference = 2 * (rectangle_width + rectangle_length)

# Define the dimensions of the circle
circle_diameter = 34  # in meters
circle_radius = circle_diameter / 2

# Calculate the area and circumference of the circle
circle_area = math.pi * (circle_radius ** 2)
circle_circumference = 2 * math.pi * circle_radius

# Print the results
print(f"Rectangle Area: {rectangle_area:.2f} square meters")
print(f"Rectangle Circumference: {rectangle_circumference:.2f} meters")
print(f"Circle Area: {circle_area:.2f} square meters")
print(f"Circle Circumference: {circle_circumference:.2f} meters")
