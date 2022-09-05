import json


def parser(file):
    with open(f'json/{file}', 'r', encoding='utf-16-be') as json_file:
        data = json_file.read()
        result = json.loads(data)
        prop = str(result['has']).replace(':', '').replace('{', '')\
            .replace('}', '').replace("'", "")
    print(f"User's name is {result['name']}, he lives in {result['city']}. "
          f"He have {len(result['children'])} children's. His property are {prop}")


parser('user1.json')
parser('user2.json')
parser('user3.json')
