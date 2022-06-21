while True:


    def calculator():
        a_a = float(input('Enter the first value '))
        b_b = float(input('Enter the second value '))
        c_c = input('Enter the operator ((+, -, /, *, dif) ')
        if c_c == '+':
            result = a_a + b_b
        elif c_c == '-':
            result = a_a - b_b
        elif c_c == '*':
            result = a_a * b_b
        elif b_b != 0:
            if c_c == '/':
                result = a_a / b_b
            elif c_c == 'dif':
                result = a_a // b_b
        elif b_b == 0:
            result = 'Division by zero is not possible!!!'
        return result


    print(calculator())
# added function 'dif'