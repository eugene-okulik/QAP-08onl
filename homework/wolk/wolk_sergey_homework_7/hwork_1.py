ALPHABET = ('абвгдеёжзиклмнопрстуфхчшщъыьэюя'
            'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
def encryption_caesar(msg, SET_S):
    encrypted_alphabet = ALPHABET[SET_S:] + ALPHABET[:SET_S]
    encrypted = []
    for char in msg:
        index = get_char_index(char, ALPHABET)
        encrypted_char = encrypted_alphabet[index] if index >= 0 else char
        encrypted.append(encrypted_char)
    return ''.join(encrypted)
def get_char_index(char, alphabet):
    char_index = alphabet.find(char)
    return char_index
def decryption_caesar(msg, offset=None):
    encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
    decrypted = []
    if not offset:
        dictionary = ['Привет', 'пока', 'что']
        for offset in range(len(ALPHABET)):
            encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
            for char in msg:
                index = get_char_index(char, encrypted_alphabet)
                encrypted_char = ALPHABET[index] if index >= 0 else char
                decrypted.append(encrypted_char)
            decrypted = ''.join(decrypted)
            word: str
            for word in dictionary:
                if word in decrypted:
                    return decrypted
            decrypted = []
    else:
        for char in msg:
            index = get_char_index(char, encrypted_alphabet)
            encrypted_char = encrypted_alphabet[index - offset] \
                if index >= 0 else char
            decrypted.append(encrypted_char)
        return ''.join(decrypted)
    return f'Не удалось расшифровать сообщение {msg:f}'
if __name__ == '__main__':
    MESS = 'Привет! Мир'
    ST = 5
    ENCRYPTED_MESSAGE = encryption_caesar(MESS, ST)
    print(f'Введите Сообщение: {MESS:f}')
    print(f'Зашифрованное сообщение: {ENCRYPTED_MESSAGE:f}')
    print(f'Расшифрованное сообщение: {decryption_caesar(ENCRYPTED_MESSAGE):f}')
