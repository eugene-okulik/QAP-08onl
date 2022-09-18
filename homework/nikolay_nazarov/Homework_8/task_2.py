from random import randint

number_names = {
    0: 'zero', 1: 'one', 3: 'three', 2: 'two',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: "fifteen",
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def num_list_generator(len_of_list=99):
    return [randint(0, 19) for i in range(len_of_list)]


def my_sort_func(some_list_to_sort):
    i = 0
    while i < len(some_list_to_sort):
        try:
            if number_names[some_list_to_sort[i]] < number_names[some_list_to_sort[i+1]]:
                i += 1
            elif number_names[some_list_to_sort[i]] == number_names[some_list_to_sort[i+1]]:
                i += 1
            else:
                temp = some_list_to_sort[i]
                some_list_to_sort[i] = some_list_to_sort[i + 1]
                some_list_to_sort[i + 1] = temp
                i = 0
        except IndexError:
            break
    return some_list_to_sort


Random_list = num_list_generator(10)
print(Random_list)
print(my_sort_func(Random_list))
