ALPHABET = ('абвгдеёжзиклмнопрстуфхчшщъыьэюя'
            'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
def encryption_caesar(msg, offset):
    encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
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
    if offset:
        for char in msg:
            index = get_char_index(char, encrypted_alphabet)
            encrypted_char = encrypted_alphabet[index - offset] \
                if index >= 0 else char
            decrypted.append(encrypted_char)
        return ''.join(decrypted)
    else:
        dictionary = ['Привет', 'пока', 'что']
        for offset in range(len(ALPHABET)):
            encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
            for char in msg:
                index = get_char_index(char, encrypted_alphabet)
                encrypted_char = ALPHABET[index] if index >= 0 else char
                decrypted.append(encrypted_char)
            decrypted = ''.join(decrypted)
            for word in dictionary:
                if word in decrypted:
                    return decrypted
            decrypted = []
    return 'Не удалось расшифровать сообщение %s' % msg
if __name__ == '__main__':
    message = 'Привет! Мир'
    shift = 5
    encrypted_message = encryption_caesar(message, shift)
    print('Сообщение: %s' % message)
    print('Зашифрованное сообщение: %s' % encrypted_message)
    print('Расшифрованное сообщение: %s' % decryption_caesar(encrypted_message))
