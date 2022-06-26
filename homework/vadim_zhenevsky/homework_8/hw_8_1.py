first_1 = int(input("Введите первое число: "))
second_2 = int(input("Введите второе число: "))


def decorator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif first < second:
            operation = "/"
        return func(first, second, operation)

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == "*":
        print(first * second)
    elif operation == "+":
        print(first + second)
    elif operation == "-":
        print(first - second)
    elif operation == "/":
        print(first / second)


calc(first_1, second_2, decorator)
