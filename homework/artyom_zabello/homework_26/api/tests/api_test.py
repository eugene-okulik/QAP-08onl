import allure
import requests
from ..utils.utils_api import ApiMethods, Utils
from ..utils.files_json import JsonFiles

TOKEN = Utils.get_new_token(domain='http://167.172.172.115:52353')


@allure.suite("API tests")
def test_create_meme(domain):
    with allure.step('Create'):
        res_json = JsonFiles.json_create_meme('bad meme', 'https://123.com', 'cool', 'big')
        result: requests.Response = ApiMethods.create_new_meme(domain, res_json, TOKEN)
        assert 'bad meme' in result.json()['text'] and result.status_code == 200


@allure.suite("API tests")
def test_update_meme(domain):
    with allure.step('Update'):
        json1 = JsonFiles.json_create_meme('bad meme', 'https://123.com', 'cool', 'big')
        result_post: requests.Response = ApiMethods.create_new_meme(domain, json1, TOKEN)
        id_previous = result_post.json()['id']
        json2 = JsonFiles.json_update_meme(id_previous, 'good meme')
        result_put: requests.Response = ApiMethods.update_meme(domain, id_previous, json2, TOKEN)
        assert 'good meme' in result_put.json()['text'] and result_put.status_code == 200


@allure.suite("API tests")
def test_delete_meme(domain):
    with allure.step('Delete'):
        json1 = JsonFiles.json_create_meme('bad meme', 'https://123.com', 'cool', 'big')
        result_post: requests.Response = ApiMethods.create_new_meme(domain, json1, TOKEN)
        id_previous = result_post.json()['id']
        result1: requests.Response = ApiMethods.delete_meme(domain, id_previous, TOKEN)
        result2: requests.Response = ApiMethods.get_meme_by_id(domain, TOKEN, id_previous)
        assert f'Meme with id {id_previous} successfully deleted' in result1.text \
               and result2.status_code == 404


@allure.suite("API tests")
def test_get_all_memes(domain):
    with allure.step('Get all memes'):
        result: requests.Response = ApiMethods.get_all_memes(domain, TOKEN)
        print(result.text)
        assert len(result.json()['data']) > 0 and result.status_code == 200
