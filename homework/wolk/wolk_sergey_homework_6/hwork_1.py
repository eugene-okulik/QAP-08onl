STR1 = input("Input: ")


def COUNT(line):
    line += 'n'
    LIST1 = []
    STR_L = len(line)
    RES_STR = ""

    counter = 1

    for i in range(0, STR_L - 1):
        if line[i] == line[i + 1]:
            counter += 1
        else:
            LIST1.append({line[i]: counter})
            counter = 1

    for element in LIST1:
        for key, value in element.items():
            RES_STR += key
            if value > 1:
                RES_STR += str(value)

    return RES_STR


print(COUNT(STR1))
