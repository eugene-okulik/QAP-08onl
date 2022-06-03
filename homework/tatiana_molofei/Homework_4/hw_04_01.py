# Напишите программу, которая добавляет ‘ing’ к словам в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

my_list = text.split()
my_list_1 = my_list.append(' ')

TEXT_1 = 'ing '.join(my_list)
TEXT_2 = TEXT_1.replace(",ing", "ing,")
TEXT_3 = TEXT_2.replace(".ing", "ing.")
print(TEXT_3)
