# Program: Square it Out

# Step 1: Ask the user for numbers (separated by spaces)
numbers = input("Enter numbers separated by spaces: ").split()

# Step 2: Convert input strings to integers
numbers = [int(num) for num in numbers]

# Step 3: Create an empty list to store squares
squares = []

# Step 4: Loop through each number and calculate its square
for num in numbers:
    squares.append(num ** 2)

# Step 5: Display the results
print("\nNumbers: ", numbers)
print("Squares: ", squares)
