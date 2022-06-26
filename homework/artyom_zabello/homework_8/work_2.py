from random import randint

number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

lst = []
lst2 = []
lexical_order = dict(sorted((number_names.items()), key=lambda x: x[1]))
for num in range(1, randint(10, 20)):
    lst.append(randint(0, 19))
for num in lexical_order.keys():
    for num2 in lst:
        if num == num2:
            lst2.append(num2)

print(f"Первоначальный набор цифр : {lst}")
print(f"Отсортированный набор цифр : {lst2}")
