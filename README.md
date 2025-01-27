![ ](https://github.com/webbrowser11/ching/actions/workflows/python-publish.yml/badge.svg)

# ching
money money money!
## about
ching is a money tracking library for python!
## never wanted to track your money
this is the library for you!
it has built in money tracking functions and more!
it also has security and blocks you from ecxeeding your moneylimit (made in the: moneylimit(NumberValue) function.)
## install
install latest version: `pip install ching` (recommended)
install certain version `pip install ching==(version)` (not recommended)
## simple commands
```
ching.limitmoney(NumberValue) # limit the amount of money able to be held in the tracking file.
ching.getdate() # logs the date so it knows when to add allowances and income days
ching.finddate() # find the date from the date logs, useful for allowance and income day tracking
ching.addmoney(NumberValue) # add an amount of money to the tracking file.
ching.minusmoney(NumberValue) # minus an amount of money from the tracking file.
ching.printmoney() # print the amount of money in your tracking file
```
all examples [here](https://github.com/webbrowser11/ching/blob/main/examples/Main.py)
