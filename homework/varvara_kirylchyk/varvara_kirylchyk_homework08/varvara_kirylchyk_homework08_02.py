# На вход подаётся некоторое количество (не больше сотни)
# разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).

# Выведите их через пробел в порядке лексикографического возрастания
# названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2

# поскольку слово two в словаре встречается позже слова three, а слово three
# -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)

# number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
# 6: 'six', 7: 'seven', 8: 'eight',
# 				9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
# 				14: 'fourteen', 15: 'fifteen',
# 				16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

# from num2words import num2words
# print(num2words(9))

NUMBERS_STR = "1 2 2 1 2 3 4 5"

number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

print(sorted([int(i) for i in NUMBERS_STR.split()], key=lambda x: number_names[x]))

# list1 = []
# for e in numbers_str.split():
#     list1.append(number_names[int(e)])
# print(list1)
#
# new_list = sorted(list1)
# print(new_list)
#
# list2 = []
# def get_key_by_value(my_dict, value):
#     for k, v in my_dict.items():
#         if v == value:
#             return k
#
# for e in new_list:
#     list2.append(get_key_by_value(number_names, e))
#
# print(list2)
