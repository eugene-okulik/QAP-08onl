def calculator(choice, a_a, b_b):
    if choice == 1:
        result = a_a+b_b
    elif choice == 2:
        result = a_a-b_b
    elif choice == 3:
        result = a_a*b_b
    elif choice == 4:
        if b_b == 0:
            result = "Division by 0"
        else:
            result = "Quotient " + str(int(a_a / b_b)) + "Remains " + str(int(a_a % b_b))
    else:
        result = "Not correct"
    return result


op_r = int(input("""Choose operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division\n"""))

first_num = float(input("Type first number:\n"))
second_num = float(input("Type second number:\n"))

print(calculator(op_r, first_num, second_num))
