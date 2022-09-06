import json


def user_info(files):
    with open(f'json_data/{files}', 'r', encoding="utf-8") as json_file:
        info = json_file.read()
        # print(info)
    analysed_info = json.loads(info)
    # print(analysed_info)
    kids = analysed_info['children']
    kids = " and ".join(kids)
    # print(kids)
    user_own = str(analysed_info['has']).replace(':', '').replace('{', '').replace('}', ''). \
        replace("'", "")
    print(f"User name is {analysed_info['name']}, he lives in {analysed_info['city']}. He has "
          f"{len(analysed_info['children'])} children - {kids}. He owns {user_own}.")


user_info('file_1.json')
user_info('file_2.json')
user_info('file_3.json')
