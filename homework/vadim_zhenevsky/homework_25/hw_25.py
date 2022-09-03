import json


def users_info(users):
    with open(f'data_json/{users}', encoding="utf8") as json_file:
        content = json_file.read()
        parsed_content = json.loads(content)
        things_owned = str(parsed_content['has']).replace(':', '').replace('{', '') \
            .replace('}', '').replace("'", "")
    print(f"User name is {parsed_content['name']}. He lives in {parsed_content['city']}. "
          f"He has {len(parsed_content['children'])} kids. "
          f"He owns a {things_owned}.")


users_info('user1.json')
users_info('user2.json')
users_info('user3.json')
