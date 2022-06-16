def encode(text, shift):
    """This function converts a input string to string
    at caesar 's cipher case"""
    lst = []
    for char in text.lower():
        if char != " " and char not in "?.,!?;:_-":
            res = ord(char) + shift
            if res > 122:
                res = 96 + (res - 122)
                lst.append(chr(res))
            else:
                lst.append(chr(res))
        else:
            lst.append(char)
    return "".join(lst)


def decode(text, shift):
    """This function decodes a string from caesar 's cipher"""
    lst = []
    for char in text.lower():
        if char != " " and char not in "?.,!?;:_-":
            res = ord(char) - shift
            if res < 97:
                res = 122 - (97-res)
                lst.append(chr(res))
            else:
                lst.append(chr(res))
        else:
            lst.append(char)
    return "".join(lst)


print(encode(input(), int(input())))
print(decode(input(), int(input())))
