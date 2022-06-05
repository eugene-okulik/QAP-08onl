# Напишите программу, которая добавляет ‘ing’
# к словам в тексте “Etiam tincidunt neque erat,
# quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero”

text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

text = text.replace(',', '').replace('.', '')
for word in text:
    text_1 = (' '.join(f'{word}ing ' for word in text.split()))
print(text_1)
