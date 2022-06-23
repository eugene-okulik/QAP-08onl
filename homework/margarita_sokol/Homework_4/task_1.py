# Напишите программу, которая добавляет ‘ing’ к словам в тексте.

MY_TEXT = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
          'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

MY_TEXT1 = MY_TEXT.replace(' ', 'ing ')
MY_TEXT2 = MY_TEXT1.replace(',ing', 'ing,')
MY_TEXT3 = MY_TEXT2.replace('.ing','ing.')
MY_TEXT4 = MY_TEXT3.replace('o', 'oing')
print(MY_TEXT4)
