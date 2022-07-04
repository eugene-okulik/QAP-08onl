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
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50руб
книга 200руб
ручка 100руб
карандаш 70руб
альбом 120руб
пенал 300руб
рюкзак 500руб'''

USER_LIST = PRICE_LIST.split()

KEY = {
    USER_LIST[i]: int(USER_LIST[i + 1].replace('руб', ''))
    for i in range(0, len(USER_LIST), 2)
}

print(KEY)
