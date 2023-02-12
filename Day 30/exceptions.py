# FileNotFound
# with open("a_file.txt") as file:
# file.read()

# key error
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# Index error
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# Type error
# text = "abc"
# print(text + 5)

# Syntax
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
#     print("Do this if there was no exception")
# finally:
#     file.close()
#     print("File was closed.")
#     print("This runs always")
#     raise TypeError("This is an error that i made up")


# Example
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)
