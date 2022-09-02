from urllib import request, error
import json


def test_get_all_posts(domain):
    req = request.Request(f'{domain}/posts')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    # print(response[0]['title'])
    assert len(response) == 100


def test_get_one_post(domain):
    req = request.Request(f'{domain}/posts/15')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert response['id'] == 15


def test_create_post(domain):
    req = request.Request(f'{domain}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', 'sfsdfgsdfgsd')
    req.data = json.dumps({
        "title": "QAP08",
        "body": "QAP08 text",
        "userId": 1
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['title'] == 'QAP08'


def test_update_post(domain):
    req = request.Request(f'{domain}/posts/19')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps({
        "title": "QAP08_upd",
        "body": "QAP08 text_upd",
        "userId": 13
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['title'] == 'QAP08_upd'


def test_delete_post(domain):
    req = request.Request(f'{domain}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps({
        "title": "QAP08",
        "body": "QAP08 text",
        "userId": 1
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    post_id = response['id']
    req = request.Request(f'{domain}/posts/{post_id}')
    req.method = 'DELETE'
    response = request.urlopen(req)
    req = request.Request(f'{domain}/posts/{post_id}')
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        assert err.code == 404
        return
    assert False
