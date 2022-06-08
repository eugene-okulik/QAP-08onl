text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
my_list = text.split()
my_list_1 = my_list.append(' ')
text_1 = 'ing '.join(my_list)
text_2 = text_1.replace(",ing", "ing,")
text_3 = text_2.replace(".ing", "ing.")
print(text_3)
