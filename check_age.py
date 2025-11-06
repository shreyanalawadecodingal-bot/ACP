# Program: Check Age

# Step 1: Ask the user to enter their age
age = int(input("Enter your age: "))

# Step 2: Check the age category
if age < 0:
    print("Invalid age! Age cannot be negative.")
elif age < 18:
    print("You are a Minor.")
elif age < 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")
