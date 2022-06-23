PRICE_LIST = '''тетрадь 50р
книга 200р 
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

RES = PRICE_LIST.split()


def dict_gen():
    """This function converts from string(PRICE_LIST) to dictionary"""
    res_dict = {RES[word]: int(RES[word+1].replace('р', '')) for word in range(0, len(RES), 2)}
    return res_dict


print(dict_gen())
