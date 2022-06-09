# Напишите программу, которая добавляет ‘ing’ к словам в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

TEXT = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

TEXT = TEXT.replace(',', ' ')
TEXT = TEXT.replace('.', ' ')
TEXT = ' '.join(f'{word}ing' for word in TEXT.split())
print(TEXT)
