# есть 3  json_files файла.
# Нужно сгенерировать текст следующего вида на основе данных, имеющихся в json файлах:
# "User name is <John>, he lives in <New York>. He has <2> kid(s) - Hanna,  Peter.
# He owns car Dodge, computer Apple"
# Важно, чтобы в результате получился один код, который умеет генерировать
# этот текст из любого из этих трех файлов.

"""module"""
import json


def user_data(file):
    """module"""
    with open(f'json_files/{file}', encoding="utf8") as json_file:
        data = json_file.read()
        result_data = json.loads(data)
        own_things = str(result_data['has']).replace(':', '').replace('{', '')\
            .replace('}', '').replace("'", "")
    print(f"User name is {result_data['name']}. He lives in {result_data['city']}. "
          f"He has {len(result_data['children'])} kid(s). "
          f"He owns {own_things}.")


user_data('user1.json')
user_data('user2.json')
user_data('user3.json')
