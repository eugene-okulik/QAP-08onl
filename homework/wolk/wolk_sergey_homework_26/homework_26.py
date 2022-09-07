from urllib import request, error
import json


def test_get_all(domain):
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    response = request.urlopen(req).read().decode('utf-8')
    assert len(response) == 1


def test_get_tags(domain):
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    req.add_header('tags', 'fun')
    response = request.urlopen(req).read().decode('utf-8')
    print(response)
    assert len(response) == 1


def test_create(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
        },
        "tags": [
            "meme",
            13
        ],
        "text": "meme",
        "url": "url.com"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    print(response)
    assert response['text'] == 'meme'


def test_update(domain):
    req = request.Request(f'{domain}/meme/9', method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
        },
        "tags": [
            "meme",
            13
        ],
        "text": "meme updated",
        "url": "url.com",
        "id": 9
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == 'meme updated'

def test_delete_meme(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    req.data = json.dumps({
        "info": {
            "purpose": "delete",
            "type": "text"
        },
        "tags": [
            "meme",
            1111
        ],
        "text": "meme to delete",
        "url": "url.com"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    meme_id = response["id"]
    req = request.Request(f'{domain}/meme/{meme_id}', method='DELETE')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    print(response)
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err)
        assert err.code == 404
        return
    assert False
