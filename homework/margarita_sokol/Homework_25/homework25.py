import json


def users_text(users):
    with open(f'json_data/{users}', 'r', encoding='UTF-8') as json_file:
        content = json_file.read()
        result = json.loads(content)
        children = ' and '.join(result['children'])
        user_own = str(result['has']).replace(':', '').replace('{', '') \
            .replace('}', '').replace("'", "")
        print(f"The user's name is {result['name']}, he lives in {result['city']}. "
              f"He has {len(result['children'])} kids {children}.\n"
              f"The property has {user_own}.")


users_text('user1.json')
users_text('user2.json')
users_text('user3.json')
