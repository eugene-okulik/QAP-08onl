import random
import json

import pytest
import requests
from conftest import meme_id_to_conf


def test_meme_creation(domain, token, clean_up):
    # Создание мема
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
    meme_id = response["id"]
    # Получение мема
    url = f"{domain}/meme/{meme_id}"

    payload = {}
    headers = {
        'Authorization': f'{token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    meme_id_to_conf(meme_id)

    assert response.status_code == 200, "Статус-код не равен 200, тест провален"


def test_meme_change(domain, token, clean_up, pre_condition_meme):
    # Изменить мем
    url = f"{domain}/meme/{pre_condition_meme['meme_id']}"
    change_payload = json.dumps({
        "id": pre_condition_meme['meme_id'],
        "info": {
            "cat_info_1": "cat_info_1_value",
            "cat_info_2": "cat_info_2_value",
            "cat_info_3": "cat_info_3_value"
        },
        "tags": [
            "cat_tag_1",
            "cat_tag_2",
            "cat_tag_3"
        ],
        "text": f"cat_text1{random.randint(1, 500)}",
        "url": "cat_url",

    })
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json'
    }
    requests.request("PUT", url, headers=headers, data=change_payload)
    # Получить мем
    url = f"{domain}/meme/{pre_condition_meme['meme_id']}"

    payload = {}
    headers = {
        'Authorization': f'{token}'
    }

    response_get_text = requests.request("GET", url, headers=headers, data=payload).json()
    response_get_text.pop("updated_by")
    meme_id_to_conf(pre_condition_meme['meme_id'])
    response_get_text = json.dumps(response_get_text)

    assert change_payload == response_get_text


def test_meme_deletion(domain, token, pre_condition_meme):
    # Удаление мема
    url = f"{domain}/meme/{pre_condition_meme['meme_id']}"

    payload = {}
    headers = {
        'Authorization': f'{token}'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)
    # Получить мем
    url = f"{domain}/meme/{pre_condition_meme['meme_id']}"
    payload = {}
    headers = {
        'Authorization': f'{token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 404


def test_meme_get_all(domain, token):
    # Получить все мемы
    url = f"{domain}/meme"

    payload = {}
    headers = {
        'Authorization': f'{token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    for value in response.values():
        count_tags_fun = 0
        for tags in value:
            for tag in tags["tags"]:
                if tag == 'fun':
                    count_tags_fun += 1
        assert count_tags_fun >= 1
