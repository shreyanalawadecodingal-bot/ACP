# Program: Reverse Order (Without using inbuilt functions)

# Step 1: Ask the user to enter numbers or words
items = input("Enter numbers or words separated by spaces: ").split()

# Step 2: Create an empty list for the reversed order
reversed_items = []

# Step 3: Use a loop to manually reverse the list
for i in range(len(items) - 1, -1, -1):
    reversed_items.append(items[i])

# Step 4: Display the reversed list
print("\nItems in reverse order:")
for item in reversed_items:
    print(item, end=" ")
