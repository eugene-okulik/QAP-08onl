"""Под словарем находится решение задачи"""
# Дано: вот такой dict:
# colors = {
# 'sun': 'yellow',
# 'grass': 'green',
# 'tree': 'green',
# 'sky': 'blue',
# 'water': 'blue',
# 'clouds': 'white'}
# Выведите на экран всё, что имеет цвет green
colors = {
    'sun': 'yellow',
    'grass': 'green',
    'tree': 'green',
    'sky': 'blue',
    'water': 'blue',
    'clouds': 'white'
}
TO_PRINT = 'green'
for key, value in colors.items():
    if value == TO_PRINT:
        print(key)
