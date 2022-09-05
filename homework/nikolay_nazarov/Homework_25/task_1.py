import json

with open("json_files/user3.json", "r", encoding="utf-8") as json_file:
    parsed_content = json.load(json_file)
name = parsed_content["name"]
city = parsed_content["city"]
children_quantity = len(parsed_content["children"])
CHILDREN = parsed_content["children"]
CHILDREN = " ".join(CHILDREN)
HAS = str(parsed_content['has']).replace(':', '').replace('{', '').replace('}', '').replace("'", "")

text = f"Пользователя зовут {name}, он живет в городе {city}. " \
       f"У него есть {children_quantity} ребенка {CHILDREN}. " \
       f"В собственности есть {HAS} "
print(text)
