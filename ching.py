from datetime import datetime, timedelta
import os

money = 0
attempt_amount = 0
AddMoneyAcsess = True

# Ensure money.txt exists and initialize it with 0 if empty
def __initialize_money_file():
    global money
    if not os.path.exists("money.txt"):
        with open("money.txt", "w") as file:
            file.write("0\n")  # Initialize the file with 0

    # Read the initial amount from the file if it exists
    with open("money.txt", "r") as file:
        first_line = file.readline().strip()
        if first_line.isdigit():
            money = int(first_line)

# Update the money file with the current amount
def __update_money_file():
    with open("money.txt", "w") as file:
        file.write(f"{money}\n")  # Replace the first line with the updated amount

# Add money to allowance
def addmoney(moneytoadd):
    global money
    if AddMoneyAcsess != False:
        money += moneytoadd
        __update_money_file()
    else:
        print("sorry looks like your access to this function has been blocked for the rest of this session.")

# Subtract money from allowance
def minusmoney(moneytominus):
    global money
    money -= moneytominus
    __update_money_file()

# Print the current money amount
def printmoney():
    if AddMoneyAcsess != False:
        print(money)
    else:
        print("sorry looks like your access to this function has been blocked for the rest of this session.")

# Function to get the current date and log it to logfile.txt
def getdate():
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Check if logfile.txt exists, and read its contents if so
    if os.path.exists("logfile.txt"):
        with open("logfile.txt", "r") as file:
            lines = file.readlines()
    else:
        lines = []

    # Replace the first line with the current date
    if lines:
        lines[0] = f"{current_date}\n"
    else:
        lines.append(f"{current_date}\n")

    # Write the updated contents back to the file
    with open("logfile.txt", "w") as file:
        file.writelines(lines)

# Function to find the first line in logfile.txt
def finddate():
    try:
        with open("logfile.txt", "r") as file:
            first_line = file.readline().strip()  # Read and strip any whitespace or newline
            return first_line
    except FileNotFoundError:
        return None  # Return None if the file does not exist

# Check if the given date matches the current date based on specified interval
def incomedate(date, interval):
    global money
    given_date = datetime.strptime(date, "%m/%d/%Y")  # Convert the date to a datetime object
    today = datetime.now()  # Get today's date

    # Calculate the appropriate comparison date based on the interval
    if interval == 'daily':
        comparison_date = today
    elif interval == 'weekly':
        comparison_date = today - timedelta(weeks=1)
    elif interval == 'hourly':
        comparison_date = today - timedelta(hours=1)
    elif interval == 'yearly':
        comparison_date = today - timedelta(days=365)  # Roughly a year, can be adjusted for leap years
    else:
        print("Invalid interval specified.")
        return

    # Check if the given date falls within the specified interval
    if given_date >= comparison_date:
        print(f"You got your income for {interval}!")
        money += 100  # Increment money (example amount)
        __update_money_file()
    else:
        print("No income yet.")

# Weekly allowance function
def allowance(weekday):
    global money
    today_weekday = datetime.now().strftime("%A").lower()  # Get the current weekday as a string
    if today_weekday == weekday.lower():  # Check if today is the specified weekday
        print("It's allowance day!")
        money += 50  # Increment money (example amount for allowance)
        __update_money_file()

def limitmoney(moneylimit):
    global money
    if money > moneylimit:
        money = moneylimit
        print("money limit eceeded automatically set")
        attempt_amount =+ 1
        print("attempt logged")
    if attempt_amount == 5:
        money = moneylimit
        print("money limit reached.")
        print("acsess to the printmoney() function is denied")
        AddMoneyAcsess = False

# Initialize money file on library load
__initialize_money_file()
