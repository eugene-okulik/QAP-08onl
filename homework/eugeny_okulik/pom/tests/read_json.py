import json


with open('test_data/data.json', 'r', encoding="utf8") as json_file:
    # content = json_file.read()
    parsed_content = json.load(json_file)
# print(content)
print(parsed_content)
print(parsed_content['children'][1])
