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
