# Есть переменная с фамилией и именем: “Ivanov Ivan”.
# Распечатайте ее так, чтобы сначала шло имя, а затем фамилия.
# Т.е. “Ivan Ivanov”

STRING = 'Ivanov Ivan'
NEW_STRING = STRING.split(" ")
NEW_STRING.reverse()
FINAL_STRING = " ".join(NEW_STRING)
print(FINAL_STRING)
