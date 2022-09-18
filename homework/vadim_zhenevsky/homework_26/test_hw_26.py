import json
from urllib import request, error

with open('new_token.txt', 'r', encoding='UTF-8') as my_token_file:
    my_token = my_token_file.read()


def test_get_all_meme(domain):
    req = request.Request(f'{domain}/meme')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)


def test_existence_of_a_meme_with_the_fun_tag(domain):
    req = request.Request(f'{domain}/meme')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    for value in dict().values():
        count_tags_fun = 0
        for tags in value:
            for tag in tags["tags"]:
                if tag == 'fun':
                    count_tags_fun += 1
        assert count_tags_fun >= 1


def test_create_meme(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    req.data = json.dumps({
            "info": {
                "size": "604*604",
                "type": "fun"
            },
            "tags": [
                "QA",
                "cat"
            ],
            "text": "meme from Vadim",
            "url": "https://i07.fotocdn.net/s106/eada9f3ec2f77ca2/public_pin_l/2296407960.jpg"
        }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == 'meme from Vadim'


def test_update_meme(domain):
    req = request.Request(f'{domain}/meme/168', method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    req.data = json.dumps({
        "id": 168,
        "info": {
            "size": "604*604",
            "type": "fun"
        },
        "tags": [
            "QA",
            "cat"
        ],
        "text": "meme from Vadim_upd",
        "url": "https://i07.fotocdn.net/s106/eada9f3ec2f77ca2/public_pin_l/2296407960.jpg"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == 'meme from Vadim_upd'


def test_delete_meme(domain):
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    req.data = json.dumps({
            "info": {
                "size": "604*604",
                "type": "fun"
            },
            "tags": [
                "QA",
                "cat"
            ],
            "text": "meme from Vadim",
            "url": "https://i07.fotocdn.net/s106/eada9f3ec2f77ca2/public_pin_l/2296407960.jpg"
        }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    meme_id = response["id"]
    req = request.Request(f'{domain}/meme/{meme_id}', method='DELETE')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    response = request.urlopen(req)
    print(response)
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', my_token)
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err)
        assert err.code == 404
        return
    assert False
