from urllib import request, error
import json


with open('new_token.txt', 'r', encoding='UTF-8') as new_token_file:
    new_token = new_token_file.read()


def test_create_new_mem(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.data = json.dumps({"name": "anastasiya"}).encode('utf-8')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    req.data = json.dumps({
        "text": "BEFORE COFFEE/AFTER COFFEE",
        "url": "https://thatcuddlycat.com/wp-content/uploads/2021/07/coffee-cat-meme.jpg",
        "tags": [
            "mem",
            "funny",
            "cats",
            "morning"
        ],
        "info": {
            "type": "text",
            "sort": "animal_meme",
            "size": "big"
        },
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == "BEFORE COFFEE/AFTER COFFEE"


def test_update_new_mem(domain):
    req = request.Request(f'{domain}/meme/184')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    req.data = json.dumps({
        "text": "BEFORE COFFEE/AFTER COFFEE_upd",
        "url": "https://thatcuddlycat.com/wp-content/uploads/2021/07/coffee-cat-meme.jpg",
        "tags": [
            "mem",
            "funny",
            "cats",
            "early morning"
        ],
        "info": {
            "type": "text",
            "sort": "animal",
            "size": "really big"
        },
        "id": 184
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == "BEFORE COFFEE/AFTER COFFEE_upd"


def test_delete_new_mem(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', new_token)
    req.data = json.dumps({
        "text": "BEFORE COFFEE/AFTER COFFEE_upd",
        "url": "https://thatcuddlycat.com/wp-content/uploads/2021/07/coffee-cat-meme.jpg",
        "tags": [
            "mem",
            "funny",
            "cats",
            "early morning"
        ],
        "info": {
            "type": "text",
            "sort": "animal",
            "size": "really big"
        },
        "id": 184
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
    # req.add_header('Content-Type', 'application/json')
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
