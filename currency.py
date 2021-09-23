# prompt the user for number of US dollars
# int is used since we're asking for full dollar amounts
dollars = int(input("Please enter number of US dollars:\n"))

# prompt the user for the rate of conversion
# float is used because conversion rates can be decimal numbers
conversion = float(input("1 USD = ? Please input currency rate.\n"))

# prompt the user for the conversion fee
# int is used on the assumption the fee is a full dollar amount, which is fair to make since we're only reporting the units of foreign currency as full
fee = int(input("Please enter the fixed conversion fee (in USD).\n"))

# tell the user the fee for buying currency
print("Fee for buying currency (in USD):" , fee)

# determine how many units remain without the fee
# int is used to report the amount of full units
difference = dollars - fee
units = int(difference * conversion)

# tell the user how many full units of foreign currency remain
print("You have" , units , "full unit(s) of foreign currency.")
