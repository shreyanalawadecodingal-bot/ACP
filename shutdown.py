# Program: Shutdown Simulation

# Step 1: Ask the user if they want to shutdown
choice = input("Do you want to shutdown the system? (yes/no): ").lower()

# Step 2: Check the choice and respond
if choice == "yes":
    print("System will shutdown now... (Simulation)")
elif choice == "no":
    print("Shutdown cancelled. The system is still running.")
else:
    print("Invalid input! Please enter 'yes' or 'no'.")
