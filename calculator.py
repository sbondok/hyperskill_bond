def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return round((n1 / n2), 2)


operations = {"+": add, "-": subtract, "*": multiply, "/": divide, }


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    end_calc = False
    while not end_calc:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        y_n = input(f"Do another operation where {answer} ends? (y/n)").lower()
        if y_n == "y":
            num1 = answer
        else:
            ask_continue = input("Do calc again from scratch (y/n)").lower()
            if ask_continue == "y":
                calculator()  # very important concept "recursion" to repeat the whole program again.
            else:
                break

calculator()