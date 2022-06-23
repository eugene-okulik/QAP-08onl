# Напишите программу, которая добавляет ‘ing’ к словам в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

TEXT = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Innteger utrna nisl, facilisis vitae semper at, dignissim vitae libero'

TEXT = TEXT.split()

A = 'ing '.join(TEXT)
B = A.replace(",ing", "ing,")
C = B.replace(".ing", "ing.")
print(C)
