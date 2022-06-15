def calculator(choice, a, b):
    if choice == 1:
        result = a+b
    elif choice == 2:
        result = a-b
    elif choice == 3:
        result = a*b
    elif choice == 4:
        if b == 0:
            result = "Division by 0"
        else:
            result = "Quotient" + str(int(a / b)) + "Remains" + str(int(a % b))
    else:
        result = "Not correct"
    return result


OP = int(input("""Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division\n"""))

FIRST = float(input("Type first number:\n"))
SECOND = float(input("Type second number:\n"))

print(calculator(OP, FIRST, SECOND))
