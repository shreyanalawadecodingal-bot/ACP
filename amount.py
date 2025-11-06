# Program: Due Amount Calculator

# Step 1: Ask the user for total amount and amount paid
total_amount = float(input("Enter the total amount: "))
amount_paid = float(input("Enter the amount paid: "))

# Step 2: Calculate the due amount
due_amount = total_amount - amount_paid

# Step 3: Check if there is any due or overpayment
if due_amount > 0:
    print(f"The due amount is: {due_amount}")
elif due_amount == 0:
    print("No due amount. Payment is complete!")
else:
    print(f"Overpayment of {-due_amount} detected. Please refund!")
