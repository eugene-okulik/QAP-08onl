"""System module."""
# Задание
# В папке json_files находится 3 json файла.
# Нужно сгенерировать текст следующего вида на основе данных, имеющихся в json файлах:
# "User name is <John>, he lives in <New York>. He has <2> kid(s) - Hanna,  Peter.
# He owns car Dodge, computer Apple"
# Важно, чтобы в результате получился один код, который умеет генерировать
# этот текст из любого из этих трех файлов.


import json


def parse(file):
    """A dummy docstring."""
    with open(f'json_files/{file}', encoding="utf8") as json_file:
        data = json_file.read()
        result = json.loads(data)
        own_things = str(result['has']).replace(':', '').replace('{', '')\
            .replace('}', '').replace("'", "")
    print(f"User name is {result['name']}. He lives in {result['city']}. "
          f"He has {len(result['children'])} kid(s). "
          f"He owns {own_things}.")


parse('user1.json')
parse('user2.json')
parse('user3.json')
