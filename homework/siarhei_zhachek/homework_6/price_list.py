PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

MY_DICT = dict((position, int(price.strip('р')))
               for position, price in (element.split()
                                       for element in PRICE_LIST.split('\n')))
print(MY_DICT)
