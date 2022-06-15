alfabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
            , 'u', 'v', 'w', 'x', 'y', 'z']

a = "hello world!"
offset = 3
i = 0
a = 0
decoded_alfabet = []
while a < len(alfabet1):
    try:
        decoded_alfabet.append(alfabet1[i+3])
        i += 1
        a += 1
    except IndexError:
        i = 0
        while a < len(alfabet1):
            decoded_alfabet.append(alfabet1[i])
            i += 1
            a += 1
dictionary = {i: k for i, k in alfabet1, decoded_alfabet}


print(alfabet1)
print(decoded_alfabet)
print(dictionary)
# decoded_alfabet = [alfabet[alfabet.index(i)+3] for i in alfabet]

#print(decoded_alfabet)

