import pytest
import json
import requests


DOMAIN = "http://167.172.172.115:52353"


@pytest.fixture(scope='function')
def domain():
    yield DOMAIN


@pytest.fixture(scope='function')
def token():
    with open('token.txt', 'r', encoding='UTF-8') as token_file:
        token = token_file.read()
    response = requests.request('GET', f'{DOMAIN}/authorize/{token}')
    if response.status_code == 200:
        pass
    else:
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps(
            {
                'name': 'Sergey_z'
            }
        )
        response = requests.request('POST', f'{DOMAIN}/authorize', headers=headers, data=data).json()
        with open('token.txt', 'w', encoding='UTF-8') as token_f:
            token_f.write(response['token'])
        token_f.close()
    with open('token.txt', 'r', encoding='UTF-8') as token_file:
        token = token_file.read()
    yield token
    token_file.close()


@pytest.fixture(scope='function')
def meme_text():
    with open(f'data_json/my_meme.json', 'r', encoding='UTF-8') as meme_file:
        new_meme = meme_file.read()
    new_meme = json.loads(new_meme)
    yield new_meme
    meme_file.close()


@pytest.fixture(scope='function')
def changing_meme():
    with open(f'data_json/changing_meme_text.json', 'r', encoding='UTF-8') as meme_change:
        change_meme = meme_change.read()
    new_meme = json.loads(change_meme)
    yield new_meme
    meme_change.close()


@pytest.fixture(scope='function')
def deleted_meme():
    with open(f'data_json/text_for_delete_meme.json', 'r', encoding='UTF-8') as meme_delete:
        delete_meme = meme_delete.read()
    meme = json.loads(delete_meme)
    yield meme
    meme_delete.close()
