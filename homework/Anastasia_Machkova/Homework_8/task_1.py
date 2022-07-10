first_ = int(input("Enter first number "))
second_ = int(input("Enter second number "))


def my_dec(func):
    def wrapper(first, second, operation):
        if first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif second > first:
            operation = "/"
        elif first < 0 or second < 0:
            operation = "*"
        return func(first, second, operation)

    return wrapper


@my_dec
def calc(first, second, operation):
    if operation == "+":
        print(first + second)
    elif operation == "-":
        print(first - second)
    elif operation == "/":
        print(first / second)
    elif operation == "*":
        print(first * second)


calc(first_, second_, my_dec)
