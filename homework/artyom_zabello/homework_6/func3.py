PRICE_LIST = '''тетрадь 50р
книга 200р 
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

RES = PRICE_LIST.split()
LST = []


def dict_gen():
    """This function converts from string(PRICE_LIST) to dictionary"""
    for i in RES:
        if not i.isalpha():
            for x_1 in i:
                if x_1 == "р":
                    LST.append(i.replace(x_1, ""))
        elif i.isalpha():
            LST.append(i)
    res_dic = {LST[i]: LST[i + 1] for i in range(0, len(LST), 2)}
    return res_dic


print(dict_gen())
