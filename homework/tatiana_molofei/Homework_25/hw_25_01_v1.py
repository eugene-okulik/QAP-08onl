import json


with open('user2.json', encoding="utf8") as f:
    templates = json.load(f)
# with open('user2.json') as f:
#     templates = json.load(f)
# with open('user3.json') as f:
#     templates = json.load(f)

user_name = templates['name']
user_city = templates['city']
user_children = templates['children']
user_own = templates['has']

child_name = []

for i in user_children:
    child_name.append(i)

own_things = []

for things, name_things in user_own.items():
    own_things.append(things)
    own_things.append(' ')
    own_things.append(name_things)
    own_things.append(', ')


print(f'User name is {user_name}, he lives in {user_city} city. '
      f'He has {len(user_children)} children {" and ".join(child_name)}. '
      f'He owns {"".join(own_things).rstrip(own_things[-1])}.')
