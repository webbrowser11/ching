# ching.py

# ching, the money tracking library!!!!

money = 0

def addmoney(moneytoadd):
    global money
    money = money + moneytoadd
def minusmoney(moneytominus):
    global money
    money = money - moneytominus
def printmoney():
    print(money)