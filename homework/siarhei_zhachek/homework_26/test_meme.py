import json
import requests


def test_a_meme_has_been_created(domain, meme_text, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = json.dumps(meme_text)
    response = requests.request('POST', f'{domain}/meme', headers=headers, data=data).json()
    assert response['text'] == 'What you will see is called a meme.'


def test_changing_the_meme(domain, changing_meme, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = json.dumps(changing_meme)
    response = requests.request('PUT', f'{domain}/meme/12', headers=headers, data=data).json()
    assert response["text"] == 'What you will see is called a meme, cool memes!!!.'


def test_delete_mem(domain, deleted_meme, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    data = json.dumps(deleted_meme)
    response = requests.request(
        'POST',
        f'{domain}/meme',
        headers=headers,
        data=data
    ).json()
    meme_id = response['id']
    requests.request('DELETE', f'{domain}/meme/{meme_id}', headers=headers, data=data)
    response = requests.request('GET', f'{domain}/meme/{meme_id}', headers=headers, data=data)
    assert response.status_code == 404


def test_existence_of_a_meme_with_the_fun_tag(domain, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = requests.request('GET', f'{domain}/meme', headers=headers).json()
    for value in dict(response).values():
        count_tags_fun = 0
        for tags in value:
            for tag in tags["tags"]:
                if tag == 'fun':
                    count_tags_fun += 1
        assert count_tags_fun >= 1
