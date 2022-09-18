from urllib import request, error
import json


with open('new_token.txt', 'r', encoding='UTF-8') as new_token_file:
    new_token = new_token_file.read()


def test_create_new_mem(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    req.data = json.dumps({
        "text": "Margarita mem",
        "url": "https://www.cdn.memify.ru/media/9__dtJDANcMsR7ImG0yu4A/20220910/q6G599lA7oo.jpg",
        "tags": [
            "mem",
            'funny'
            "text"
            "cats",
        ],
        "info": {
            "popularity": "high",
            "size": "big",
            "type": "text"
         },
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == "Margarita mem"


def test_update_new_mem(domain):
    req = request.Request(f'{domain}/meme/77')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    req.data = json.dumps({
        "text": "Margarita mem updated",
        "url": "https://www.cdn.memify.ru/media/9__dtJDANcMsR7ImG0yu4A/20220910/q6G599lA7oo.jpg",
        "tags": [
            "mem",
            "cute cats",
        ],
        "info": {
            "popularity": "high",
            "size": "average",
        },
        "id": 77
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == "Margarita mem updated"


def test_delete_new_mem(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    req.data = json.dumps({
        "text": "Margarita mem updated",
        "url": "https://www.cdn.memify.ru/media/9__dtJDANcMsR7ImG0yu4A/20220910/q6G599lA7oo.jpg",
        "tags": [
            "mem",
            "cute cats",
        ],
        "info": {
            "popularity": "high",
            "size": "average",
        },
        "id": 77
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    meme_id = response["id"]
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.method = 'DELETE'
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    response = request.urlopen(req)
    print(response)
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err)
        assert err.code == 404
        return
    assert False


def test_find_meme_with_word_fun(domain):
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', new_token)
    req.add_header("tags", "fun")
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
