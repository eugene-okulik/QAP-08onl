# Напишите программу, которая добавляет ‘ing’ к словам в тексте “Etiam tincidunt neque erat,
# quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”

SOME_TEXT = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
            "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
WORDS = SOME_TEXT.split()
MODDED_WORDS = []
for i in WORDS:
    if i.endswith("."):
        i = i[:-1]+"ing."
        MODDED_WORDS.append(i)
    elif i.endswith(","):
        i = i[:-1]+"ing,"
        MODDED_WORDS.append(i)
    else:
        i = i + "ing"
        MODDED_WORDS.append(i)
print(' '.join(MODDED_WORDS))
