# Program: Square Pattern

# Step 1: Ask the user for the size of the square
size = int(input("Enter the size of the square: "))

# Step 2: Loop to print rows
for i in range(size):
    # Print stars in each row
    for j in range(size):
        print("*", end=" ")
    # Move to the next line
    print()
