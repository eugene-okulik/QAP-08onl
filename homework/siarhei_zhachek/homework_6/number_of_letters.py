STR_A = "aaadddce"
RESULT = ''
for i in set(STR_A):
    RESULT = RESULT + i + str(STR_A.count(i))
print(RESULT.replace('1', ''))
