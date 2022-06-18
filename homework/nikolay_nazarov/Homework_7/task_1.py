"""Программа декодирует шифр Цезаря"""
alfabet_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

INPUT_STRING_FOR_ENCODING = "Hello world"
INPUT_STRING_FOR_DECODING = "vszzc kcfzr"


def decoder(some_text_to_decode, step):
    index_counter = 0
    counter_len = 0
    encoded_alfabet = []
    while counter_len < len(alfabet_eng):
        try:
            encoded_alfabet.append(alfabet_eng[index_counter + step])
            index_counter += 1
            counter_len += 1
        except IndexError:
            index_counter = 0
            while counter_len < len(alfabet_eng):
                encoded_alfabet.append(alfabet_eng[index_counter])
                index_counter += 1
                counter_len += 1
    decode_dictionary = dict(zip(encoded_alfabet, alfabet_eng))

    some_text_to_decode = some_text_to_decode.lower()
    some_text_decoded = ""
    decoder_counter = 0
    while decoder_counter < len(some_text_to_decode):
        if some_text_to_decode[decoder_counter] != " " \
                and some_text_to_decode[decoder_counter] != "!":
            some_text_decoded += (decode_dictionary[some_text_to_decode[decoder_counter]])
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

def encoder(some_text_to_encode, step):
    index_counter = 0
    counter_len = 0
    encoded_alfabet = []
    while counter_len < len(alfabet_eng):
        try:
            encoded_alfabet.append(alfabet_eng[index_counter + step])
            index_counter += 1
            counter_len += 1
        except IndexError:
            index_counter = 0
            while counter_len < len(alfabet_eng):
                encoded_alfabet.append(alfabet_eng[index_counter])
                index_counter += 1
                counter_len += 1
    encode_dictionary = dict(zip(alfabet_eng, encoded_alfabet))

    some_text_to_encode = some_text_to_encode.lower()
    some_text_encoded = ""
    decoder_counter = 0
    while decoder_counter < len(some_text_to_encode):
        if some_text_to_encode[decoder_counter] != " " \
                and some_text_to_encode[decoder_counter] != "!":
            some_text_encoded += (encode_dictionary[some_text_to_encode[decoder_counter]])
            decoder_counter += 1
        elif some_text_to_encode[decoder_counter] == " ":
            some_text_encoded += " "
            decoder_counter += 1
            continue
        elif some_text_to_encode[decoder_counter] == "!":
            some_text_encoded += "!"
            decoder_counter += 1
            continue
    return some_text_encoded


print(decoder(INPUT_STRING_FOR_DECODING, 14))
print(encoder(INPUT_STRING_FOR_ENCODING, 14))
