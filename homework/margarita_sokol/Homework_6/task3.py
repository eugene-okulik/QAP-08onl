# Дан такой кусок прайс листа:

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# При помощи генераторов превратите этот текст в словарь такого вида:
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70,
# 'альбом': 120, 'пенал': 300, 'рюкзак': 500}

MY_PRICE_LIST = PRICE_LIST.split()
LENGHT = len(MY_PRICE_LIST)
LIST = []
for i in range(0, LENGHT):
    if i % 2 != 0:
        MY_PRICE_LIST[i] = int(MY_PRICE_LIST[i].rstrip('р'))
for q in range(0, LENGHT):
    if q % 2 == 0:
        PAIRS = [MY_PRICE_LIST[q], MY_PRICE_LIST[q+1]]
        LIST.append(PAIRS)
DICTIONARY = {key: value for key, value in LIST}
print(DICTIONARY)
