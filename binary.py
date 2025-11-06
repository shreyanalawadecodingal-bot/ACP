# Program: Binary Conversion without inbuilt functions

# Step 1: Ask the user for a decimal number
num = int(input("Enter a decimal number: "))

# Step 2: Initialize an empty string to store binary
binary = ""

# Step 3: Special case for 0
if num == 0:
    binary = "0"
else:
    # Step 4: Loop to convert decimal to binary
    n = num
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary  # add remainder at the front
        n = n // 2

# Step 5: Display the result
print(f"Binary of {num} is: {binary}")
