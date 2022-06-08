# Напишите программу, которая добавляет ‘ing’ к словам в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

MY_STRING = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
          'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
MY_STRING1 = MY_STRING.replace(' ', 'ing ')
MY_STRING2 = MY_STRING1.replace(',ing', 'ing,')
MY_STRING3 = MY_STRING2.replace('o', 'oing')
MY_STRING4 = MY_STRING3.replace('l.', 'ling.')
print(MY_STRING4)
