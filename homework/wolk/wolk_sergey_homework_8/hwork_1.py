INPUT_1 = int(input("Введите первое число \f"))
OUTPUT_1 = int(input("Введите второе число \f"))


def count(func):
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


@count
def secondary_count(first, second, operation):
    if operation == '+':
        result = first + second
    if operation == '-':
        result = first - second
    if operation == '/':
        result = first / second
    if operation == '*':
        result = first * second
    return result


print(secondary_count(INPUT_1, OUTPUT_1, "+"))
