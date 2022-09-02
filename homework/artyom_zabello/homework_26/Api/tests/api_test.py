import allure
import requests
from ..utils.utils_api import ApiMethods, Utils

TOKEN = Utils.get_new_token(domain='http://167.172.172.115:52353')


@allure.suite("API tests")
def test_create_meme(domain):
    with allure.step('Create'):
        file = 'Api/utils/create_meme.json'
        text = Utils.read_file(file)['text']
        result: requests.Response = ApiMethods.create_new_meme(domain, TOKEN, file)
        print(result.text)
        assert text in result.json()['text'] and result.status_code == 200


@allure.suite("API tests")
def test_update_meme(domain):
    with allure.step('Update'):
        file = 'Api/utils/update_meme.json'
        text = Utils.read_file(file)['text']
        result: requests.Response = ApiMethods.update_meme(domain, 10, file, TOKEN)
        print(result.text)
        assert text in result.json()['text'] and result.status_code == 200


@allure.suite("API tests")
def test_delete_meme(domain):
    with allure.step('Delete'):
        result1: requests.Response = ApiMethods.delete_meme(domain, 10, TOKEN)
        result2: requests.Response = ApiMethods.get_meme_by_id(domain, TOKEN, 10)
        assert 'Meme with id 10 successfully deleted' in result1.text \
               and result2.status_code == 404


@allure.suite("API tests")
def test_get_all_memes(domain):
    with allure.step('Get all memes'):
        result: requests.Response = ApiMethods.get_all_memes(domain, TOKEN)
        print(result.text)
        assert len(result.json()['data']) > 0 and result.status_code == 200












