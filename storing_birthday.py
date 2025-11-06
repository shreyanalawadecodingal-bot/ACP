# Program: Storing Birthdays

# Step 1: Create a dictionary to store names and birthdays
birthdays = {
    "Alice": "12 April 2001",
    "Bob": "5 September 1999",
    "Charlie": "22 January 2003"
}

# Step 2: Show available names
print("Welcome to the Birthday Database!")
print("We have birthdays for:")
for name in birthdays:
    print("-", name)

# Step 3: Ask the user whose birthday they want
name = input("\nEnter a name to look up their birthday: ")

# Step 4: Display the result
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have a birthday recorded for {name}.")

# Step 5 (optional): Add a new birthday
choice = input("\nDo you want to add a new birthday? (yes/no): ").lower()
if choice == "yes":
    new_name = input("Enter the person's name: ")
    new_birthday = input("Enter their birthday (e.g., 15 March 2002): ")
    birthdays[new_name] = new_birthday
    print(f"{new_name}'s birthday has been added!")

print("\nUpdated Birthday List:")
for name, date in birthdays.items():
    print(f"{name}: {date}")
