# file = open("my_file.txt")
# contents = file.read()
# print(contents)
#
# file.close()

# Better approach
# mode w -> replaces the content
# mode a -> append the content
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("new_file.text", mode="w") as file:
    file.write("\nNew text inside new_file.")
