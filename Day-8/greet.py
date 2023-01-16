
# Simple function
def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice today?")


greet()

# Function with input


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Vishal")

# Function with more than one input


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Vishal", "Mysore")
greet_with(location="Bangalore", name="Vishal")
