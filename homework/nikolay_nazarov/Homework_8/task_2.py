from random import randint

number_names = {
    0: 'zero', 1: 'one', 3: 'three', 2: 'two',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: "fifteen",
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def num_list_generator(len_of_list=99):
    return [randint(0, 19) for i in range(len_of_list)]


def dict_to_json_converter(some_dict):
    dict_convertered_to_json = {}
    i = 0
    for key, value in some_dict.items():
        dict_convertered_to_json[key] = {"word": value, "position": i}
        i += 1
    return dict_convertered_to_json


def my_sort_func(some_list_to_sort, dict_for_sorting):
    i = 0
    while i < len(some_list_to_sort):
        try:
            if dict_for_sorting[some_list_to_sort[i]]["position"] \
                    < dict_for_sorting[some_list_to_sort[i + 1]]["position"]:
                i += 1
            elif dict_for_sorting[some_list_to_sort[i]]["position"] \
                    == dict_for_sorting[some_list_to_sort[i + 1]]["position"]:
                i += 1
            else:
                temp = some_list_to_sort[i]
                some_list_to_sort[i] = some_list_to_sort[i + 1]
                some_list_to_sort[i + 1] = temp
                i = 0
        except IndexError:
            break
    return some_list_to_sort


# Сгенерируем рандомный список где какждое значение равно случайному значению от 0 до 19.
# В функции укажем длинну списка (по умолчанию 99)
Random_list = num_list_generator(10)
print(Random_list)
# Сгенерируем словарь на основе number_names ,
# который будет иметь следующую структуру каждого элемента:
# {0: {'word': 'zero', 'position': 0}
# В качестве аргумента вводим словарь из условия задачи(number_names)
Extended_dict = dict_to_json_converter(number_names)
# И наконец, отсортируем рандомный список Random_list на основе дополненного словаря Extended_dict
List_sorted = my_sort_func(Random_list, Extended_dict)
# Выведем элементы полученного списка в одну строку черех пробел
for elem in List_sorted:
    print(elem, end=' ')
