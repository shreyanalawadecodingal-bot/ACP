# Program: Summer Times (Sum of Numbers)

# Step 1: Ask the user how many numbers they want to add
count = int(input("How many numbers do you want to add? "))

# Step 2: Initialize sum
total = 0

# Step 3: Loop to get numbers from user and add them
for i in range(count):
    num = float(input(f"Enter number {i + 1}: "))
    total += num

# Step 4: Display the result
print("\n☀️ The total sum of the numbers is:", total)
