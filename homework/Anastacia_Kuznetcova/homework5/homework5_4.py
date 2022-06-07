# Поступил приказ об увеличении зарплаты всех начальников отделов на 500.
# Нужно изменить salary всем у кого title = head
# Измените словарь так, чтобы ЗП у всех, у кого нужно увеличилась на 500.
# Выведите на экран тот словарь, который в итоге получится.
"""Внизу решение задачи"""
DEPARTMENTS = {
    'sales': {
        'Ivanov': {
            'title': 'head',
            'salary': 5000
        },
        'Petrov': {
            'title': 'manager',
            'salary': 3000
        }
    },
    'operations': {
        'Sidorov': {
            'title': 'accountant',
            'salary': 1500
        },
        'Viktorov': {
            'title': 'head',
            'salary': 4500
        }
    }
}

for key, value in DEPARTMENTS.items():
    for key2, value2 in value.items():
        if value2['title'] == 'head':
            value2['salary'] += 500
print(DEPARTMENTS)
