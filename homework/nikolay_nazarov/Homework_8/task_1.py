First_num = int(input("Введите первое число\n"))
Second_num = int(input("Введите второе число\n"))


def operation_generator(func):
    def wrapper(first, second, operation):
        if first == second and not first < 0 and not second < 0:
            operation = "+"
        elif first > second and not first < 0 and not second < 0:
            operation = "-"
        elif first < second and not first < 0 and not second < 0:
            operation = "/"
        elif first < 0 or second < 0:
            operation = "*"
        return func(first, second, operation)

    return wrapper


@operation_generator
def calc(first, second, operation):
    if operation == '+':
        result = first + second
    if operation == '-':
        result = first - second
    if operation == '/':
        result = first / second
    if operation == '*':
        result = first * second
    return result


print(calc(First_num, Second_num, "+"))
