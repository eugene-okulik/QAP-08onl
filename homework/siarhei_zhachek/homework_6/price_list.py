PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
MY_STR = PRICE_LIST.replace('0р', '0')
MY_LIST = MY_STR.split('\n')
NEW_LIST = []
for positions in MY_LIST:
    NEW_LIST.append(positions.split())
print({key: value for key, value in NEW_LIST})
