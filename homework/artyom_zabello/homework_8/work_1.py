num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def decar(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        if first == second:
            operation = "+"
        if first > second:
            operation = "-"
        if first < second:
            operation = "/"
        return func(first, second, operation)

    return wrapper


@decar
def calc(first, second, operation):
    if operation == "*":
        print(first * second)
    if operation == "+":
        print(first + second)
    if operation == "-":
        print(first - second)
    if operation == "/":
        print(first / second)


calc(num1, num2, decar)
