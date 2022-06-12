# Поступил приказ об увеличении зарплаты всех начальников отделов на 500.
# Нужно изменить salary всем у кого title = head
# Измените словарь так, чтобы ЗП у всех, у кого нужно увеличилась на 500.
# Выведите на экран тот словарь, который в итоге получится.

departments = {
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

for key, value in departments.items():
    for key_1, value_1 in value.items():
        if value_1['title'] == 'head':
            value_1['salary'] += 500


print(departments)
