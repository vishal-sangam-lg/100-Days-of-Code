# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Assumption that you live 60 years
years = 60 - int(age)
months = years * 12
weeks = years * 52
days = years * 365

# Old way
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# New way
print("You have {} days, {} weeks, and {} months left.".format(days, weeks, months))

