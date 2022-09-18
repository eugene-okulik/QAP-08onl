import json


def users_info(users):
    with open(f'data_json/{users}', 'r', encoding='UTF-8') as json_file:
        content = json_file.read()
    parsed_content = json.loads(content)
    children = ' and '.join(parsed_content['children'])
    user_own = str(parsed_content['has']).replace(':', '').replace('{', ''). \
        replace('}', '').replace("'", "")
    print(f"User name is {parsed_content['name']}, he lives in {parsed_content['city']} city.\n"
          f"He has {len(parsed_content['children'])} children {children}.\n"
          f"He owns {user_own}.")


users_info('user1.json')
users_info('user2.json')
users_info('user3.json')
