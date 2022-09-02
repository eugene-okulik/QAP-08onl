import requests
import json


def test_get_all_posts(domain):
    response = requests.request('GET', f'{domain}/posts').json()
    print(response)
    assert len(response) == 100


def test_get_one_post(domain):
    response = requests.request('GET', f'{domain}/posts/19').json()
    assert response['id'] == 19


def test_create_post(domain):
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "title": "QAP08_upd",
        "body": "QAP08 text_upd",
        "userId": 13
    })
    response = requests.request(
        'POST',
        f'{domain}/posts',
        headers=headers,
        data=data
    ).json()
    assert response['title'] == 'QAP08_upd'


def test_update_post(domain):
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "title": "QAP08_upd",
        "body": "QAP08 text_upd",
        "userId": 13
    })
    response = requests.request(
        'PUT',
        f'{domain}/posts/19',
        headers=headers,
        data=data
    ).json()
    assert response['userId'] == 13


def test_delete_post(domain):
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "title": "QAP08_upd",
        "body": "QAP08 text_upd",
        "userId": 13
    })
    response = requests.request(
        'POST',
        f'{domain}/posts',
        headers=headers,
        data=data
    ).json()
    post_id = response['id']
    requests.request('DELETE', f'{domain}/posts/{post_id}')
    response = requests.request('GET', f'{domain}/posts/{post_id}')
    assert response.status_code == 404
