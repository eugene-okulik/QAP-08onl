# Дан такой кусок прайс листа:
# (Копируйте эту переменную (константу) в код прямо как есть)

# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''

# При помощи генераторов превратите этот текст в словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100,
# 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в скобках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

x = PRICE_LIST.split("\n")

output = {}

for line in x:
    item = line.split()
    output.update({item[0]: int(item[1][:-1])})

#print(output)

for keys,values in output.items():
    print(keys, values)

# def every_second_element(values):
#     second_values = []
#
#     for index in range(1, len(values), 2):
#         second_values.append(values[index])
#
#     return second_values
#
# # print(every_second_element(x))
#
# y = every_second_element(x)
# # print(y)
#
# # new_y=[s.replace("p", "") for s in y]
# new_y=[s.replace("р", "") for s in y]
#
# new_numbers = []
# for n in new_y:
#     new_numbers.append(int(n))
# new_y = new_numbers
#
# # print(new_y)
#
# def every_second_element2(values):
#     second_values = []
#
#     for index in range(0, len(values), 2):
#         second_values.append(values[index])
#
#     return second_values
#
# # print(every_second_element2(x))
# w = every_second_element2(x)
# # print(w)
#
# # w = key
# # new_y = value
#
# res = {}
# for key in w:
#     for value in new_y:
#         res[key] = value
#         z = new_y.remove(value)
#         break
#
# print(res)

# def is_palindrom(line):
#     if line == line[::-1]:
#         return True
#     return False
