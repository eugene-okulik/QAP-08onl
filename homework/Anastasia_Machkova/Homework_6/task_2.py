def calculator(choice, A, B):
    if choice == 1:
        result = A+B
    elif choice == 2:
        result = A-B
    elif choice == 3:
        result = A*B
    elif choice == 4:
        if B == 0:
            result = "Division by 0"
        else:
            result = "Quotient" + str(int(A / B)) + "Remains" + str(int(A % B))
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
