# Calculator
from art import logo


# ADD
def add(n1, n2):
    return n1 + n2


# SUBTRACT
def subtract(n1, n2):
    return n1 - n2


# MULTIPLY
def multiply(n1, n2):
    return n1 * n2


# DIVIDE
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print("{} {} {} = {}".format(num1, operation_symbol, num2, answer))

        if input(f"Type 'y' to continue Calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
