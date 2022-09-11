import requests
import json


def test_meme_creation(domain, token):
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
    print(response.json()["id"])
    assert response.status_code == 200, "Статус-код не равен 200, тест провален"
    # Удаление мема
    url = f'{domain}/meme/{meme_id}'

    payload = {}
    headers = {
        'Authorization': f'{token}'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
