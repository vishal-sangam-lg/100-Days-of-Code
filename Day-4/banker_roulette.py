import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total = len(names)
random_number = random.randint(0, total-1)
choice = names[random_number]
print("{} is going to buy the meal today!".format(choice))
