# Program: Product of all elements in a tuple

# Step 1: Define or input a tuple
# Example tuple
numbers = (2, 3, 4, 5)

# Step 2: Initialize a variable to store the product
product = 1

# Step 3: Loop through each element in the tuple and multiply
for num in numbers:
    product *= num

# Step 4: Display the result
print(f"The tuple is: {numbers}")
print(f"The product of all elements is: {product}")
