import requests
import json


class Utils:
    @staticmethod
    def get_new_token(domain):
        query = {"name": "Artyom"}
        req = requests.post(f'{domain}/authorize', json=query)
        token = req.json()['token']
        result = {"Authorization": token}
        return result

    @staticmethod
    def read_file(file_name):
        with open(f"{file_name}", 'r') as file:
            res = json.loads(file.read())
        return res


    #
    # @staticmethod
    # def check_token(domain, token):
    #     req = requests.get(f'{domain}/authorize/{token}')
    #     if 'Token is alive. Username is' in req.text:
    #         return True
    #     return False


class ApiMethods:

    @staticmethod
    def create_new_meme(domain, token, file_name):
        with open(f"{file_name}", 'r') as file:
            res_json = json.loads(file.read())
        req = requests.post(f'{domain}/meme', json=res_json, headers=token)
        print(req.json())
        return req

    @staticmethod
    def update_meme(domain, id_meme, file_name, token):
        with open(f"{file_name}", 'r') as file:
            res_json = json.loads(file.read())
        req = requests.put(f'{domain}/meme/{id_meme}', json=res_json, headers=token)
        print(req.json())
        return req

    @staticmethod
    def delete_meme(domain, id_meme, token):
        req = requests.delete(f'{domain}/meme/{id_meme}', headers=token)
        return req

    @staticmethod
    def get_all_memes(domain, token):
        req = requests.get(f'{domain}/meme', headers=token)
        return req

    @staticmethod
    def get_meme_by_id(domain, token, id_meme):
        req = requests.get(f'{domain}/meme/{id_meme}', headers=token)
        return req
