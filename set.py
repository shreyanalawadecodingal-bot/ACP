# Program: Symmetric Difference of Two Sets

# Step 1: Define or input two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Step 2: Calculate symmetric difference
sym_diff = set1.symmetric_difference(set2)
# Alternative: sym_diff = set1 ^ set2

# Step 3: Display the result
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Symmetric Difference: {sym_diff}")
