# Напишите программу, которая добавляет ‘ing’
# к словам в тексте “Etiam tincidunt neque erat,
# quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero”

TEXT = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

MY_LIST = TEXT.split(' ')
MY_LIST_2 = []
for value in MY_LIST:
    if value.endswith('.'):
        MY_LIST_2.append(value[:len(value) - 1] + 'ing.')
    elif value.endswith(','):
        MY_LIST_2.append(value[:len(value) - 1] + 'ing,')
    else:
        MY_LIST_2.append(value + 'ing')
print(' '.join(MY_LIST_2))
