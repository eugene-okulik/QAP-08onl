#Есть переменная с фамилией и именем: “Ivanov Ivan”.
# Распечатайте ее так, чтобы сначала шло имя, а затем фамилия. Т.е. “Ivan Ivanov”


STR = ['Ivanov Ivan']
STR.reverse.split(' ')[::-1]

print(STR)
