# Program: Mirrored Triangle

# Step 1: Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Step 2: Loop through each row
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(i):
        print("*", end="")
    # Move to the next line
    print()
