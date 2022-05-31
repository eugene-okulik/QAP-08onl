from statistics import mean

from math import sqrt


# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел
NUM_1 = 3
NUM_2 = 9
numbers_list = {3, 9}
avg = mean(numbers_list)
print(f"Cреднее арифметическое = {avg}")
result = sqrt(NUM_1 * NUM_2)
print(f"Cреднее геометрическое = {result}")
