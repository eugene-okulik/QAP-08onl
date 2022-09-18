"""Внизу решение задания"""
WORD1 = input("Введите строку ")
WORD_CIPHER = WORD1.lower()


def encode(word_cipher):
    """Функция для шифрования строки"""
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    move = int(input('введите длину сдвига: '))
    answer = ''
    for i in word_cipher:
        if i in alphabet:
            ind = alphabet.find(i)
            new_letter = alphabet[ind + move]
            answer += new_letter
        else:
            answer += i

    return answer


print(encode(WORD_CIPHER))

WORD2 = input("Введите строку ")
DECIPHERING_THE_WORLD = WORD2.lower()


def decode(deciphering_the_word):
    """Функция для расшифрования строки"""
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    move = int(input('введите длину сдвига: '))
    answer = ''
    for i in deciphering_the_word:
        if i in alphabet:
            ind = alphabet.find(i)
            new_letter = alphabet[ind - move]
            answer += new_letter
        else:
            answer += i

    return answer


print(decode(DECIPHERING_THE_WORLD))
