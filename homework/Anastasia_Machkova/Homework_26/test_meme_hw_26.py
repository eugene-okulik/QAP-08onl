from urllib import request, error
import json


def test_new_token(domain):
    data = json.dumps({"name": "anastasia"}).encode('utf-8')
    req = request.Request(f'{domain}/authorize', method='POST', data=data)
    req.add_header("Content-Type", 'application/json')
    response = request.urlopen(req)
    token = json.loads(response.read().decode())['token']
    print(token)
    return token


NEW_TOKEN = test_new_token(domain='http://167.172.172.115:52353/')


def test_create_meme(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', NEW_TOKEN)
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
        },
        "tags": [
            "meme",
            "fun",
            "Lord of the rings"
        ],
        "text": "You can't just go and become a meme",
        "url": "https://ion.ranepa.ru/upload/medialibrary/309/novost_2.png"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == "You can't just go and become a meme"


def test_meme_changed(domain):
    req = request.Request(f'{domain}/meme/174')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', NEW_TOKEN)
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
        },
        "tags": [
            "meme",
            "fun",
            "Lord of the rings"
        ],
        "text": "You can't just go and become a meme_updated",
        "url": "https://ion.ranepa.ru/upload/medialibrary/309/novost_2.png",
        "id": 174
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == "You can't just go and become a meme_updated"


def test_delete_meme(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', NEW_TOKEN)
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
        },
        "tags": [
            "meme",
            "fun",
            "Lord of the rings"
        ],
        "text": "You can't just go and become a meme",
        "url": "https://ion.ranepa.ru/upload/medialibrary/309/novost_2.png",
        "id": 174
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    meme_id = response['id']
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.method = 'DELETE'
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', NEW_TOKEN)
    response = request.urlopen(req)
    print(response)
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', NEW_TOKEN)
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err)
        assert err.code == 404
        return
    assert False


def test_fun_tag(domain):
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', NEW_TOKEN)
    req.add_header('tags', 'fun')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    for value in dict(response).values():
        tags_fun = 0
        for tags in value:
            for tag in tags["tags"]:
                if tag == "fun":
                    tags_fun += 1
        assert tags_fun >= 1
