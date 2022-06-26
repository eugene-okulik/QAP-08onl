MASSEGE = input('Enter the encryption message ')


def encode(massage):
    alfhabet = 'abcdefghijklmnopqrstuvwxyz'
    step = int(input('Enter the encryption step '))
    massage_e = ''
    for element in massage.lower():
        position = alfhabet.find(element)
        position2 = position + step
        if element in alfhabet:
            massage_e += alfhabet[position2]
        else:
            massage_e += element
    return massage_e


print(encode(MASSEGE))
print()
MASSEGE_DECODE = input('Enter the encryption message ')


def decode(massage_decode):
    alfhabet = 'abcdefghijklmnopqrstuvwxyz'
    step = int(input('Enter the encryption step '))
    massage4 = ''
    for element in massage_decode.lower():
        position = alfhabet.find(element)
        position2 = position - step
        if element in alfhabet:
            massage4 += alfhabet[position2]
        else:
            massage4 += element
    return massage4


print(decode(MASSEGE_DECODE))
