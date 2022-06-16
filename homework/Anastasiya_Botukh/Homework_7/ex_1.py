STRING_ENCODE = str(input('Please, enter the words to encode:'))
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encode_string(string, shift):
    encode = ''
    for value in string:
        index = ALPHABET.find(value)
        if index > int(25 - int(shift)):
            index = shift - (len(ALPHABET) - 1 - index) - 1
        if index == -1:
            encode += value
        else:
            encode += ALPHABET[index + int(shift)]
    return encode


def decode_string(string, shift):
    decode = ''
    for value in string:
        index = ALPHABET.find(value)
        if index == -1:
            decode += value
        if index < int(shift):
            _ = len(ALPHABET) - 1 - (shift - index)
        else:
            decode += ALPHABET[index - int(shift)]
    return decode


RESULT = encode_string(STRING_ENCODE, 3)
print(encode_string(STRING_ENCODE, 3))
