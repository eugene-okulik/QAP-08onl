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
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120,
#  'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в скобках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

DICT_1 = PRICE_LIST.split()
EVEN = [i for i in DICT_1 if not DICT_1.index(i) % 2]
ODD = [i for i in DICT_1 if DICT_1.index(i) % 2]
print({value1: int(value2.replace('р', '')) for value1, value2 in zip(EVEN, ODD)})

# previous variant also works
# LIST = PRICE_LIST.split("\n")
# new_dict = {}
#
# for i in LIST:
#     item = i.split()
#     new_dict.update({item[0]: int(item[1][:-1])})
#
# print(new_dict)
