from datetime import datetime, timedelta
import os

money = 0
attempt_amount = 0
AddMoneyAccess = True

# Initialize money.txt if it doesn’t exist or contains invalid data
def __initialize_money_file():
    global money
    if not os.path.exists("money.txt"):
        with open("money.txt", "w") as file:
            file.write("0\n")  

    with open("money.txt", "r") as file:
        first_line = file.readline().strip()
        if first_line.isdigit():
            money = int(first_line)
        else:
            money = 0  # Reset invalid data
            __update_money_file()

# Update the money amount in money.txt
def __update_money_file():
    with open("money.txt", "w") as file:
        file.write(f"{money}\n")

# Add money (if access is allowed)
def addmoney(moneytoadd):
    global money
    if AddMoneyAccess:
        money += moneytoadd
        __update_money_file()
    else:
        print("Access to addmoney() is blocked for this session.")

# Subtract money from allowance
def minusmoney(moneytominus):
    global money
    money -= moneytominus
    __update_money_file()

# Show the current money balance
def printmoney():
    if AddMoneyAccess:
        print(money)
    else:
        print("Access to printmoney() is blocked for this session.")

# Log today’s date in logfile.txt (used for tracking allowances)
def getdate():
    current_date = datetime.now().strftime("%Y-%m-%d")

    if os.path.exists("logfile.txt"):
        with open("logfile.txt", "r") as file:
            lines = file.readlines()
    else:
        lines = []

    if lines:
        lines[0] = f"{current_date}\n"
    else:
        lines.append(f"{current_date}\n")

    with open("logfile.txt", "w") as file:
        file.writelines(lines)

# Get the last recorded date from logfile.txt
def finddate():
    try:
        with open("logfile.txt", "r") as file:
            first_line = file.readline().strip()
            return first_line if first_line else None
    except FileNotFoundError:
        return None

# Check if it's time to receive income based on a given interval
def incomedate(date, interval):
    global money
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")  
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    today = datetime.now()
    intervals = {
        "daily": today,
        "weekly": today - timedelta(weeks=1),
        "hourly": today - timedelta(hours=1),
        "yearly": today - timedelta(days=365),
    }

    comparison_date = intervals.get(interval)
    if not comparison_date:
        print("Invalid interval specified.")
        return

    if given_date >= comparison_date:
        print(f"You received your {interval} income!")
        money += 100  
        __update_money_file()
    else:
        print("No income yet.")

# Give weekly allowance on a specified weekday (but only once per day)
def allowance(weekday):
    global money
    today_weekday = datetime.now().strftime("%A").lower()
    last_allowance_date = finddate()

    if today_weekday == weekday.lower():
        if last_allowance_date != datetime.now().strftime("%Y-%m-%d"):  
            print("It's allowance day! 💰")
            money += 50  
            __update_money_file()
            getdate()  
        else:
            print("Allowance already given today.")

# Prevent the balance from exceeding a set limit & restrict access after too many attempts
def limitmoney(moneylimit):
    global money, attempt_amount, AddMoneyAccess
    if money > moneylimit:
        money = moneylimit
        print("Money limit exceeded, automatically adjusted.")
        attempt_amount += 1
        print(f"Attempt logged. Attempts so far: {attempt_amount}")

    if attempt_amount >= 5:
        money = moneylimit
        print("Money limit reached. Access to printmoney() and addmoney() is now denied.")
        AddMoneyAccess = False

# Initialize money file when script runs
__initialize_money_file()
