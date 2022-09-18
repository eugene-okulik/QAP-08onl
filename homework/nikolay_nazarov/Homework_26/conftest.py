import json

import pytest
import requests

DOMAIN = 'http://167.172.172.115:52353'
MEME_ID_CONF = None


@pytest.fixture(scope='session')
def domain():
    yield DOMAIN


@pytest.fixture(scope='session')
def token(domain):
    url = f'{domain}/authorize'

    payload = json.dumps({
        "name": "Николай Назаров"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    token = response["token"]
    yield token


@pytest.fixture(scope='function')
def clean_up(domain, token):
    yield
    url = f'{domain}/meme/{MEME_ID_CONF}'
    payload = {}
    headers = {
        'Authorization': f'{token}'
    }

    requests.request("DELETE", url, headers=headers, data=payload)


@pytest.fixture(scope='function')
def pre_condition_meme(domain, token):
    url = f'{domain}/meme'
    payload = json.dumps({
        "text": "cat_text",
        "url": "cat_url",
        "tags": [
            "cat_tag_1",
            "cat_tag_2",
            "cat_tag_3"
        ],
        "info": {
            "cat_info_1": "cat_info_1_value",
            "cat_info_2": "cat_info_2_value",
            "cat_info_3": "cat_info_3_value"
        }
    })
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    pre_condition_meme_id = response["id"]
    pre_condition_meme = {
        'meme_id': pre_condition_meme_id,
        'meme_text': f"{response['text']}",
    }
    yield pre_condition_meme


def meme_id_to_conf(meme_id):
    global MEME_ID_CONF
    MEME_ID_CONF = meme_id
