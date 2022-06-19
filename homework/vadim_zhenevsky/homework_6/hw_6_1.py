STR = "cccbba"
RESULT = ''
for i in set(STR):
    RESULT = RESULT + i + str(STR.count(i))
print(RESULT.replace('1', ''))
