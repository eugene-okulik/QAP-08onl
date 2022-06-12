PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST_KEY = [i for i in PRICE_LIST.split() if PRICE_LIST.split().index(i) % 2 != 1]
PRICE_LIST_VALUE = [int(i[:len(i)-1]) for i in PRICE_LIST.split()
                    if PRICE_LIST.split().index(i) % 2 == 1]
PRICE_LIST_DICTIONARY = dict(zip(PRICE_LIST_KEY, PRICE_LIST_VALUE))
print(PRICE_LIST_DICTIONARY)
