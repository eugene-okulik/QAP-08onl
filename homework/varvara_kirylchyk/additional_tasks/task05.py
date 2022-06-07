# Дано: вот такой dict:
# colors = {
# 'sun': 'yellow',
# 'grass': 'green',
# 'tree': 'green',
# 'sky': 'blue',
# 'water': 'blue',
# 'clouds': 'white'
# }
# Выведите на экран всё, что имеет цвет green

colors = {
'sun': 'yellow',
'grass': 'green',
'tree': 'green',
'sky': 'blue',
'water': 'blue',
'clouds': 'white'
}

CHECK = 'green'

for key, value in colors.items():
    if value in CHECK:
        print (key)
