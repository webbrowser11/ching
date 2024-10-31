# Example usage of the ching module functions

import ching

# Initialize the money file not meant to be used for public use but is here on library load if needed use this function if money tracking file is not behaving
ching.__initialize_money_file()

# Add money to allowance
ching.addmoney(50)
print("After adding money:")
ching.printmoney()  # Should print the updated money

# Subtract money from allowance
ching.minusmoney(20)
print("After subtracting money:")
ching.printmoney()  # Should print the updated money

# Log the current date
ching.getdate()
print("Logged today's date.")

# Find the first line in logfile.txt
first_date = ching.finddate()
print(f"First date in logfile: {first_date}")

# Check for income based on a specific date and interval
# Example: Check for daily income
ching.incomedate("10/31/2024", "daily")
print(f"Current money after daily income check: {ching.money}")

# Example: Check for weekly income
ching.incomedate("10/24/2024", "weekly")
print(f"Current money after weekly income check: {ching.money}")

# Example: Check for hourly income
ching.incomedate("10/31/2024", "hourly")
print(f"Current money after hourly income check: {ching.money}")

# Example: Check for yearly income
ching.incomedate("10/31/2023", "yearly")
print(f"Current money after yearly income check: {ching.money}")

# Set the allowance for a specific weekday
ching.allowance("Monday")  # Change this to the current day of the week if needed
print(f"Current money after checking allowance: {ching.money}")
