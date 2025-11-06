# Program: Check frequency of elements in a list

# Step 1: Input elements from the user
elements = input("Enter elements separated by spaces: ").split()

# Step 2: Create an empty dictionary to store frequency
frequency = {}

# Step 3: Loop through the elements and count frequency
for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Step 4: Display the frequency of each element
print("\nFrequency of each element:")
for item, count in frequency.items():
    print(f"{item} : {count}")
