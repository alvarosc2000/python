
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2


operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True
    number1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What is the second number?: "))
        answer = (operations[operation_symbol](number1,number2))
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        choice = input(f"Tupe 'y' yo continue calculating with {answer}, or 'n' to start a  new calculation.")

        if choice == 'y':
            number1 = answer
        else:
            should_accumulate = False
            calculator()

calculator()