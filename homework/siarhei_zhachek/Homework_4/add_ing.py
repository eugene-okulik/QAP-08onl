MY_STR = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
         'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
MY_STR_A = MY_STR.replace(' ', 'ing ')
MY_STR_B = MY_STR_A.replace('.ing', 'ing.')
MY_STR_C = MY_STR_B.replace(',ing', 'ing,')
MY_STR_D = MY_STR_C.replace('o', 'oing')
print(MY_STR_D)
