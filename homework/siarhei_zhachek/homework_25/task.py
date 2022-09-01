import json


def user_story(users):
    with open(f'data_json/{users}', 'r', encoding='UTF-8') as json_file:
        content = json_file.read()
    user_content = json.loads(content)
    children = ' '.join(user_content['children'])
    has = [f'{k} - {v}' for k, v in dict(user_content['has']).items()]
    user_has = ', '.join(has)
    print(f"The user's name is {user_content['name']}, he lives in {user_content['city']} city.\n"
          f"He has {len(user_content['children'])} children {children}.\n"
          f"The property has {user_has}.")
    json_file.close()


user_story('user1.json')
user_story('user2.json')
user_story('user3.json')
