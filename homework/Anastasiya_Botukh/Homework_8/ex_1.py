FIRST_NUM = int(input('Please, enter the first number:'))
SECOND_NUM = int(input('Please, enter the second number:'))


def calc(func):

    def wrapper(first_num, second_num, operation):
        if first_num < 0 or second_num < 0:
            operation = '*'
        elif first_num == second_num:
            operation = '+'
        elif first_num > second_num:
            operation = '-'
        elif second_num > first_num:
            operation = '/'
        return func(first_num, second_num, operation)
    return wrapper


@calc
def operations(first_num, second_num, operation):
    if operation == '+':
        return first_num + second_num
    if operation == '-':
        return first_num - second_num
    if operation == '*':
        return first_num * second_num
    if operation == '/':
        return first_num / second_num
    return 'wrong action'


print(operations(FIRST_NUM, SECOND_NUM, operations))
