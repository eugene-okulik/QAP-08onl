import json

with open('user1.json', encoding="utf8") as f:
    user_info = f.read()
    detailed_info = json.loads(user_info)

OWN_THINGS = []
for things, name_things in detailed_info["has"].items():
    OWN_THINGS.append(things)
    OWN_THINGS.append(' ')
    OWN_THINGS.append(name_things)
    OWN_THINGS.append(', ')
OWN_THINGS = "".join(OWN_THINGS).rstrip(OWN_THINGS[-1])

print(f'User name is {detailed_info["name"]}, he lives in {detailed_info["city"]} city. '
      f'He has {len(detailed_info["children"])} children '
      f'{" and ".join(detailed_info["children"])}. '
      f'He owns {OWN_THINGS}.')
