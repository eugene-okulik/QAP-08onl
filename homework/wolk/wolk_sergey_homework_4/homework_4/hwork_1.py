TEXT = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Innteger utrna nisl, facilisis vitae semper at, dignissim vitae libero'

TEXT = TEXT.split()


LIST1 = 'ing '.join(TEXT)
LIST2 = LIST1.replace(",ing", "ing,")
LIST3 = LIST2.replace(".ing", "ing.")
print(LIST3)
