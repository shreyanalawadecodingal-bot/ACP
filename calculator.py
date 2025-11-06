# Program: Power Calculator

# Step 1: Ask the user for the base and exponent
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Step 2: Calculate the power
result = base ** exponent  # same as pow(base, exponent)

# Step 3: Display the result
print(f"\n{base} raised to the power of {exponent} is {result}")
