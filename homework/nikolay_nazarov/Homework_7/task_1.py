"""Программа декодирует шифр Цезаря"""
alfabet_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

INPUT_STRING_FOR_ENCODING = "hello world!"
INPUT_STRING_FOR_DECODING = "khoor zruog!"


def decode_and_encode_dictionaries_generator(some_alfabet):
    """
    Функция составляет словарь для декодирования и кодирования текста.
    """
    index_counter = 0
    counter_len = 0
    encoded_alfabet = []
    while counter_len < len(some_alfabet):
        try:
            encoded_alfabet.append(some_alfabet[index_counter + 3])
            index_counter += 1
            counter_len += 1
        except IndexError:
            index_counter = 0
            while counter_len < len(some_alfabet):
                encoded_alfabet.append(some_alfabet[index_counter])
                index_counter += 1
                counter_len += 1
    encode_dictionary = dict(zip(some_alfabet, encoded_alfabet))
    decode_dictionary = dict(zip(encoded_alfabet, some_alfabet))
    return [decode_dictionary, encode_dictionary]


def decoder(some_text_to_decode, decoder_dictionary):
    """
    Функция декодирует шифр цезаря, в качестве первого аргумента вводится
    текст для кодирования или декодирования, в качестве второго - словарь полученный в результате
    работы функции decode_and_encode_dictionaries_generator
     """
    some_text_decoded = ""
    decoder_counter = 0
    while decoder_counter < len(some_text_to_decode):
        if some_text_to_decode[decoder_counter] != " " \
                and some_text_to_decode[decoder_counter] != "!":
            some_text_decoded += (decoder_dictionary[some_text_to_decode[decoder_counter]])
            decoder_counter += 1
        elif some_text_to_decode[decoder_counter] == " ":
            some_text_decoded += " "
            decoder_counter += 1
            continue
        elif some_text_to_decode[decoder_counter] == "!":
            some_text_decoded += "!"
            decoder_counter += 1
            continue
    return some_text_decoded


e = decode_and_encode_dictionaries_generator(alfabet_eng)[1]
d = decode_and_encode_dictionaries_generator(alfabet_eng)[0]
# Для того чтобы закодировать текст, необходимо
# в качестве первого аргумента ввести строку для кодирования (INPUT_STRING_FOR_ENCODING),
# а в качестве второго переменную "d". """
# Для того чтобы декодировать текст, необходимо
# в качестве первого аргумента ввести строку для декодирования (INPUT_STRING_FOR_DECODING),
# а в качестве второго переменную "e". """
print(decoder(INPUT_STRING_FOR_DECODING, d))
