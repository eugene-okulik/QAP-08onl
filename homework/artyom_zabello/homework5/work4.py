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

for i, x in departments["sales"].items():
    if x["title"] == "head":
        x["salary"] += 500

for i, x in departments["operations"].items():
    if x["title"] == "head":
        x["salary"] += 500

print(departments)
