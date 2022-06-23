# Напишите программу, которая добавляет ‘ing’ к словам в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

TEXT = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
        Integer urna nisl, facilisis vitae semper at, \
        dignissim vitae libero'

A = TEXT.split()
A.append(' ')
TEXT1 = 'ing '.join(A)
TEXT2 = TEXT1.replace(",ing", "ing,")
TEXT3 = TEXT2.replace(".ing", "ing.")
print(TEXT3)
