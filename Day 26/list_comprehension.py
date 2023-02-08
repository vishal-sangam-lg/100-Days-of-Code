# Syntax: new_list = [new_item for item in old_list if condition]
# if condition is optional

# List Comprehension with list
numbers = [1, 2, 3]
new_numbers = [number + 1 for number in numbers]
another_list = [number for number in numbers]
print(new_numbers)
print(another_list)

# List Comprehension with string
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

# List Comprehension with range()
new_range = [num * 2 for num in range(1, 5)]
print(new_range)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# Exercise 1 - Squaring Numbers
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)

# Exercise 2 - Filtering Even Numbers
even_numbers = [number for number in numbers if number & 1 == 0]
print(even_numbers)

# Exercise 3 - Data Overlap -> Intersection of numbers in file1.txt and file2.txt
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

intersection = [int(number) for number in file_1_data if number in file_2_data]
print(intersection)
