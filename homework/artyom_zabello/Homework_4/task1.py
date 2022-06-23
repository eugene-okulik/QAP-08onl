TEXT = ('Etiam tincidunt neque erat, quis molestie enim'
        'imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero').split()
LST = []
for i in TEXT:
    LST.append(i+"ing")
LST = " ".join(LST).replace(",ing", "ing,").replace(".ing", "ing.")
print(LST)
