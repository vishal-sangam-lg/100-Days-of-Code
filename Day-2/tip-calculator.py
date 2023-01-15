# Project 2 - Tip calculator

print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
tip = float(bill) * float(int(tip_percentage)/100)
bill_with_tip = float(bill) + tip
result = bill_with_tip/int(people)
print("Each person should pay: ${:.2f}".format(result))
