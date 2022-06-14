str1 = input("Input: ")


def count_log(line):
    line += 'n'
    list1 = []
    str_l = len(line)
    res_str = ""

    counter = 1

    for i in range(0, str_l - 1):
        if line[i] == line[i + 1]:
            counter += 1
        else:
            list1.append({line[i]: counter})
            counter = 1

    for element in list1:
        for key, value in element.items():
            res_str += key
            if value > 1:
                res_str += str(value)

    return res_str


print(count_log(str1))
