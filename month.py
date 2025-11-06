import calendar

# Function to return the number of days in a month
def days_in_month(year, month):
    # monthrange returns (weekday of first day, number of days)
    return calendar.monthrange(year, month)[1]

# Main program
year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month number (1-12): "))

# Call the function
num_days = days_in_month(year, month)

print(f"The month {month} of year {year} has {num_days} days.")
