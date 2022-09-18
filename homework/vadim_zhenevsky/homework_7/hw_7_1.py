word = input('Enter your message: ').lower()
shift = int(input('Enter shift length: '))
ALPHABET = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def encode(text_1):
    result_1 = ''
    for letter_1 in text_1:
        if letter_1 in ALPHABET:
            position_now = ALPHABET.find(letter_1)
            new_position = position_now + shift
            result_1 += ALPHABET[new_position]
        else:
            result_1 += letter_1
    return result_1


print(encode(word))


word_2 = input('Enter your message: ').lower()
shift_2 = int(input('Enter shift length: '))


def decode(text_2):
    result_2 = ''
    for letter_2 in text_2:
        if letter_2 in ALPHABET:
            position_now = ALPHABET.find(letter_2)
            new_position = position_now - shift_2
            result_2 += ALPHABET[new_position]
        else:
            result_2 += letter_2
    return result_2


print(decode(word_2))
