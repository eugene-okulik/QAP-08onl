#Напишите программу, которая добавляет ‘ing’ к словам в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

MY_STRING = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
            ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

MY_LIST = MY_STRING.split()
MY_NEW_LIST=[]

for word in MY_LIST:
    if word[-1] in ".,":
        new_word = word[:-1]+ 'ing'+word[-2:]
        MY_NEW_LIST.append(new_word)
    else:
        new_word = word + 'ing'
        MY_NEW_LIST.append(new_word)

MY_NEW_SRTING = ' '.join(MY_NEW_LIST)
print(MY_NEW_SRTING)
