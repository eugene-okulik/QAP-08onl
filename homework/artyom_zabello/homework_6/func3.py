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
    for word in RES:
        if not word.isalpha():
            for char in word:
                if char == "р":
                    LST.append(word.replace("р", ""))
        elif word.isalpha():
            LST.append(word)
    res_dict = {LST[i]: int(LST[i + 1]) for i in range(0, len(LST), 2)}
    return res_dict


print(dict_gen())
