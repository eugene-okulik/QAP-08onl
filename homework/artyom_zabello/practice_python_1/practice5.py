colors = {
    'sun': 'yellow',
    'grass': 'green',
    'tree': 'green',
    'sky': 'blue',
    'water': 'blue',
    'clouds': 'white'
}
for x in colors.items():
    if 'green' in x:
        for res in x:
            if res not in "green":
                print(res)
