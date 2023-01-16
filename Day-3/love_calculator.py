# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

digit1 = 0
digit2 = 0
digit1 += name1.count('t')
digit1 += name1.count('r')
digit1 += name1.count('u')
digit1 += name1.count('e')
digit1 += name2.count('t')
digit1 += name2.count('r')
digit1 += name2.count('u')
digit1 += name2.count('e')

digit2 += name1.count('l')
digit2 += name1.count('o')
digit2 += name1.count('v')
digit2 += name1.count('e')
digit2 += name2.count('l')
digit2 += name2.count('o')
digit2 += name2.count('v')
digit2 += name2.count('e')

score = str(digit1) + str(digit2)
score = int(score)
if score < 10 or score > 90:
    print("Your score is {}, you go together like coke and mentos.".format(score))
elif 40 < score < 50:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))
