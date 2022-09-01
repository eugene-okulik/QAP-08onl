import json


with open('test_data/data.json', 'r', encoding="utf8") as json_file:
    content = json_file.read()
parsed_content = json.loads(content)
print(content)
print(parsed_content)
print(parsed_content['children'][1])
