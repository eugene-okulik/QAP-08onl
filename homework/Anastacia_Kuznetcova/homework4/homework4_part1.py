# Напишите программу, которая добавляет ‘ing’ к словам в тексте “Etiam tincidunt neque erat,
# quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
TEXT = ('Etiam tincidunt neque erat, quis molestie enim '
        'imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
COMMA = TEXT.replace(',', '')
DOTS = COMMA.replace('.', '')
my_list = DOTS.split()
my_list_1 = my_list.append(' ')
print('ing '.join(my_list))
