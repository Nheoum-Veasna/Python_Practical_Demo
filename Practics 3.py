# Function to check if a number is a prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
# Lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is prime
    if is_prime(number):
        print(f"{number} is a prime number")

    # Check if the number is even or odd
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Display even and odd numbers
print("\nEven numbers from 1 to 100:")
print(even_numbers)

print("\nOdd numbers from 1 to 100:")
print(odd_numbers)
