# DS2000 Grace Michael

totalchange = int(input("Enter price in cents (1-100):\n"))

# determine amount of each
quarters = totalchange // 25

dimes = (totalchange - (quarters * 25)) // 10

nickels = (totalchange - (quarters * 25) - (dimes * 10)) // 5

pennies = (totalchange - (quarters * 25) - (dimes * 10) - (nickels * 5))

if ((totalchange // 25) >= 1):
    print("Quarters:" , quarters)
if (((totalchange - (quarters * 25)) // 10) >= 1):
    print("Dimes:" , dimes)
if ((totalchange - (quarters * 25) - (dimes * 10)) // 5 >= 1):
    print("Nickles:" , nickels)
if ((totalchange - (quarters * 25) - (dimes * 10) - (nickels * 5))):
    print("Pennies:" , pennies)
