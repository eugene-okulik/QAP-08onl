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

for department, employers in departments.items():
    for name, position in employers.items():
        if position["title"] == "head":
            position["salary"] += 500
print(departments)
