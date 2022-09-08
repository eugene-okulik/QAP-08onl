"""System module."""
# Задание - Написать 4 теста:
# 1 создание мема - проверить, что создался именно такой как вы создавали
# 2 Изменение мема - проверить, что мем изменился
# 3 Удаление мема - проверить, что мем удалился
# 4 Запросить все мемы - проверить, что существует хотя бы один мем с тегом “fun”
#
# Перед исполнением тестов нужно авторизоваться и использовать полученный токен.


from urllib import request, error
import json


def test_get_new_token(domain):
    """A dummy docstring."""
    data = json.dumps({"name": "varvara"}).encode('utf-8')
    # print(data)
    req = request.Request(f'{domain}/authorize', method='POST', data=data)
    req.add_header("Content-Type", 'application/json')
    response = request.urlopen(req)
    token = json.loads(response.read().decode())['token']
    print(token)
    return token


TOKEN = test_get_new_token(domain='http://167.172.172.115:52353')


def test_get_all_memes(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', TOKEN)
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert len(response) == 1


def test_get_tags_memes(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', TOKEN)
    req.add_header('tags', 'fun')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    # print(response)
    for value in dict(response).values():
        count_tags_fun = 0
        for tags in value:
            for tag in tags["tags"]:
                if tag == 'fun':
                    count_tags_fun += 1
        assert count_tags_fun >= 1


def test_create_meme(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', TOKEN)
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
            },
        "tags": [
            "meme",
            13
        ],
        "text": "Varvara meme",
        "url": "url.com"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == 'Varvara meme'


def test_update_meme(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme/52', method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', TOKEN)
    req.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
            },
        "tags": [
            "meme",
            13
        ],
        "text": "Varvara updated",
        "url": "url.com",
        "id": 52
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    # print(response)
    assert response['text'] == 'Varvara updated'
    req2 = request.Request(f'{domain}/meme/52', method='PUT')
    req2.add_header('Content-Type', 'application/json')
    req2.add_header('Authorization', TOKEN)
    req2.data = json.dumps({
        "info": {
            "popularity": "high",
            "type": "text"
            },
        "tags": [
            "meme",
            13
        ],
        "text": "Varvara meme",
        "url": "url.com",
        "id": 52
    }).encode('ascii')
    response2 = request.urlopen(req2).read().decode('utf-8')
    response2 = json.loads(response2)
    print(response2)


def test_delete_meme(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', 'xDw7x1tnz0mBwuQ')
    req.data = json.dumps({
        "info": {
            "purpose": "delete",
            "type": "text"
            },
        "tags": [
            "meme",
            1111
        ],
        "text": "Varvara meme to delete",
        "url": "url.com"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    meme_id = response["id"]
    req = request.Request(f'{domain}/meme/{meme_id}', method='DELETE')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', 'xDw7x1tnz0mBwuQ')
    response = request.urlopen(req)
    print(response)
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', 'xDw7x1tnz0mBwuQ')
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err)
        assert err.code == 404
        return
    assert False
