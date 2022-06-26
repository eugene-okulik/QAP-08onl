first_num = float(input('First number '))
second_num = float(input('Second number: '))


def my_calc(func):
    def wrapper(first, second, operation):
        if first < 0:
            operation = first * second
            print(operation)
        elif second < 0:
            operation = first * second
            print(operation)
        elif first == second:
            operation = first + second
            print(operation)
        elif first > second:
            operation = second - first
            print(operation)
        elif second > first:
            operation = first / second
            print(operation)

        return func(first, second, operation)
    return wrapper


@my_calc
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '*':
        print(first * second)
    elif operation == '/':
        print(first / second)


calc(first_num, second_num, my_calc)
