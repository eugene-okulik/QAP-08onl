def count():
    str_a = input('Enter the line: ')
    str_a += '.'
    my_list = []
    new_str = ''
    variable = 1
    for i in range(len(str_a)-1):
        if str_a[i] == str_a[i+1]:
            variable += 1
        else:
            my_list.append({str_a[i]: variable})
            variable = 1

    for element in my_list:
        for key, volue in element.items():
            new_str += key
            if volue > 1:
                new_str += str(volue)
    return new_str


print(count())
