import json
import requests


with open('token.txt', 'r', encoding='UTF-8') as token_file:
    token = token_file.read()


def test_a_meme_has_been_created(domain):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = json.dumps({
        "text": "What you will see is called a meme.",
        "url": "https://jrnlst.ru/sites/default/files/covers/cover_6.jpg",
        "tags": [
            "fun",
            "meme",
            "Sergey Druzhko"
         ],
        "info":
            {
                "objects":
                    ["picture",
                        "text"],
                "size":
                {
                    "width": "737",
                    "height": "1288"
                    }
            },
    })
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    assert response['text'] == 'What you will see is called a meme.'


def test_changing_the_meme(domain):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = json.dumps({
        "id": 12,
        "text": "What you will see is called a meme, cool memes!!!.",
        "url": "https://jrnlst.ru/sites/default/files/covers/cover_6.jpg",
        "tags": [
            "fun",
            "meme",
            "Sergey Druzhko",
            "bald man"
         ],
        "info":
            {
                "objects":
                    ["picture - jpg",
                        "text_rus"],
                "size":
                {
                    "width": "737",
                    "height": "1288"
                    }
            },
    })
    response = requests.request('PUT', f'{domain}/meme/12', headers=headers, data=data).json()
    assert response["text"] == 'What you will see is called a meme, cool memes!!!.'


def test_delete_mem(domain):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = json.dumps({
        "text": "my_text",
        "url": "my_url.com",
        "tags": [
            "meme",
            "bald man"
         ],
        "info":
            {
                "objects":
                    [
                        "picture",
                        "text"
                    ],
                "colors":
                    [
                        "green",
                        "black",
                        "purple"
                    ]
            }
    })
    response = requests.request(
        'POST',
        f'{domain}/meme',
        headers=headers,
        data=data
    ).json()
    meme_id = response["id"]
    requests.request('DELETE', f'{domain}/meme/{meme_id}', headers=headers, data=data)
    response = requests.request('GET', f'{domain}/meme/{meme_id}', headers=headers, data=data)
    assert response.status_code == 404


def test_existence_of_a_meme_with_the_fun_tag(domain):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    response = requests.request('GET', f'{domain}/meme', headers=headers).json()
    for value in dict(response).values():
        count_tags_fun = 0
        for tags in value:
            for tag in tags['tags']:
                if tag == 'fun':
                    count_tags_fun += 1
        assert count_tags_fun >= 1
