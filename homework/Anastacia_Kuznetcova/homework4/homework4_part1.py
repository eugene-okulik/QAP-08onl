# Напишите программу, которая добавляет ‘ing’ к словам в тексте “Etiam tincidunt neque erat,
# # quis molestie enim imperdiet vel.
# # Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
"""Внизу решение задания"""
TEXT = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
TEXT1 = TEXT.replace(' ', 'ing ')
TEXT2 = TEXT1.replace('.ing', 'ing.')
TEXT3 = TEXT2.replace(',ing', 'ing,')
TEXT4 = TEXT3.replace('o', 'oing')
print(TEXT4)
