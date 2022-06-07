# Есть переменная с фамилией и именем: “Ivanov Ivan”. /
# Распечатайте ее так, чтобы сначала шло имя, а затем фамилия. Т.е. “Ivan Ivanov”

STR = ['Ivanov Ivan']
REV = list(reversed(STR))
LIST = ' '.join(REV)
print(LIST)
