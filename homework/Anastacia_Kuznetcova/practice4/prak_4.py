# Есть переменная с фамилией и именем: “Ivanov Ivan”. Распечатайте ее так, чтобы
# сначала шло имя, а затем фамилия. Т.е. “Ivan Ivanov”
NAME_SECOND_NAME = "Ivanov Ivan"
my_list = NAME_SECOND_NAME.split()
REVERSED = list(reversed(my_list))
NO_LIST = ' '.join(REVERSED)
print(NO_LIST)
