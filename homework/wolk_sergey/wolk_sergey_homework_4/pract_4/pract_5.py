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