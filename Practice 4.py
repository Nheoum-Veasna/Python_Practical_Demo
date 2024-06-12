print("-------------------Find list Smallest and Largest number------------------------")
# List of items
numbers = [23, 22, 44, 17, 77, 55, 1, 65, 82, 2]

# Calculate the summation of the numbers
summation = sum(numbers)

# Find the smallest and largest numbers in the list
smallest_number = min(numbers)
largest_number = max(numbers)

# Print the results
print(f"Summation of the list: {summation}")
print(f"Smallest number in the list: {smallest_number}")
print(f"Largest number in the list: {largest_number}")
print("-------------------Find Reverse Tuple--------------------------------------------")
# Original tuple
original_tuple = ('A', 'I', 'B', 2022)

# Reverse the tuple
reversed_tuple = original_tuple[::-1]

# Print the result
print(f"Original tuple: {original_tuple}")
print(f"Reversed tuple: {reversed_tuple}")

print("-------------------Set Operator--------------------------------------------------")
# Define the sets
A = {1, 2, 4, 6, 7, 9, 11, 12}
B = {1, 2, 3, 5, 8, 10, 12}

# Intersection of sets
intersection = A & B

# Union of sets
union = A | B

# Set difference (A - B)
set_difference = A - B

# Symmetric difference
symmetric_difference = A ^ B

# Print the results
print(f"Intersection: {intersection}")
print(f"Union: {union}")
print(f"Set Difference (A - B): {set_difference}")
print(f"Symmetric Difference: {symmetric_difference}")

print("-------------------Define the dictionaries---------------------------------------")

# Define the dictionaries
dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}

# Combine dictionaries, creating a list of values for each key
combined_dict = {}

# Add entries from dict1
for key, value in dict1.items():
    if key not in combined_dict:
        combined_dict[key] = []
    combined_dict[key].append(value)

# Add entries from dict2
for key, value in dict2.items():
    if key not in combined_dict:
        combined_dict[key] = []
    combined_dict[key].append(value)

# Print the combined dictionary
print(f"Combined Dictionary: {combined_dict}")
