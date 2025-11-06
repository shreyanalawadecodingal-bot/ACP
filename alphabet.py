# Program: Checking Alphabets

# Step 1: Ask the user to enter a character
ch = input("Enter a character: ")

# Step 2: Check if the input is an alphabet
if ch.isalpha():
    print(f"'{ch}' is an alphabet.")
else:
    print(f"'{ch}' is NOT an alphabet.")
