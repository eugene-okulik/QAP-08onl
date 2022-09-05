import json


def users_text(users):
    with open(f'json_data/{users}', encoding="utf8") as json_file:
        data = json_file.read()
        res = json.loads(data)
        kids = ', '.join(res['children'])
        own_things = str(res['has']).replace(':', '').replace('{', '') \
            .replace('}', '').replace("'", "")
    print(f"User name is {res['name']}. He lives in {res['city']}. "
          f"He has {len(res['children'])} kid(s) : {kids}. "
          f"He owns {own_things}.")


users_text('user1.json')
users_text('user2.json')
users_text('user3.json')
