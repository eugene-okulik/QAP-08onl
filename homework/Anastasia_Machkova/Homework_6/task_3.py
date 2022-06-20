PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

ELEMENTS = PRICE_LIST.split("\n")
PAIRS = [i.split() for i in ELEMENTS]
print({k: int(v[:-1]) for k, v in PAIRS})
