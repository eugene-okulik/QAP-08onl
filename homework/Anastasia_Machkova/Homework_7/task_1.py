STRING_ENCODE = str(input("Please, enter your word: ")).lower()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def encode(string, shift):
    result = ""
    for letter in string:
        location = ALPHABET.find(letter)
        location_new = location + shift
        if letter in ALPHABET:
            result += ALPHABET[location_new]
        else:
            result += letter
    return result


def decode(string, shift):
    result_2 = ""
    for letter in string:
        location = ALPHABET.find(letter)
        location_new = location - shift
        if letter in ALPHABET:
            result_2 += ALPHABET[location_new]
        else:
            result_2 += letter
    return result_2


print(encode(STRING_ENCODE, 3))
