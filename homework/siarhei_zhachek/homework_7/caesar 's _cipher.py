alphabet = 'abcdefghijklmnopqrstuvwxyz'
step = int(input('Enter the encryption step: '))
message = input('Enter the encryption message: ')
message2 = ''
for element in message.lower():
    position = alphabet.find(element)
    position2 = position + step
    if element in alphabet:
        message2 += alphabet[position2]
    else:
        message2 += element
print(message2)
print()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
step = int(input('Enter the encryption step: '))
message = input('Enter the decryption message: ')
message2 = ''
for element in message.lower():
    position = alphabet.find(element)
    position2 = position - step
    if element in alphabet:
        message2 += alphabet[position2]
    else:
        message2 += element
print(message2)
