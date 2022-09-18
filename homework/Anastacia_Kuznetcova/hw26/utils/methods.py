import dataclasses
import requests


class Util:

    @staticmethod
    def token():
        query = {"name": "Stassia92"}
        req = requests.post('http://167.172.172.115:52353/authorize', json=query)
        token_res = req.json()['token']
        res = {"Authorization": token_res}
        return res

    @staticmethod
    def check_token(domain, token):
        req = requests.get(f'{domain}/authorize/{token}')
        if 'Token is alive. Username is' in req.text:
            return True
        return False


@dataclasses.dataclass
class ApiMethods:

    @staticmethod
    def create_new_meme(domain, file, token):
        req = requests.post(f'{domain}/meme', json=file, headers=token)
        print(req.json())
        return req

    @staticmethod
    def update_meme(domain, id_meme, file_name, token):
        req = requests.put(f'{domain}/meme/{id_meme}', json=file_name, headers=token)
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
