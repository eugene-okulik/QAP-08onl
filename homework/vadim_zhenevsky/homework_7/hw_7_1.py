word = input('Enter your message: ').lower()
shift = int(input('Enter shift length: '))
ALPHABET = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def encode(text_1):
    result_1 = ''
    for x in text_1:
        if x in ALPHABET:
            position_now = ALPHABET.find(x)
            new_position = position_now + shift
            result_1 += ALPHABET[new_position]
        else:
            result_1 += x
    return result_1


print(encode(word))


word_2 = input('Enter your message: ').lower()
shift_2 = int(input('Enter shift length: '))


def decode(text_2):
    result_2 = ''
    for y in text_2:
        if y in ALPHABET:
            position_now = ALPHABET.find(y)
            new_position = position_now - shift_2
            result_2 += ALPHABET[new_position]
        else:
            result_2 += y
    return result_2


print(decode(word_2))
