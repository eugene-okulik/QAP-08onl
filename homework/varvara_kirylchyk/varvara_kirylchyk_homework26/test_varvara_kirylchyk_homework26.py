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


def test_get_all_memes(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert len(response) == 1


# не работает :-(
def test_get_tags_memes(domain):
    """A dummy docstring."""
    req = request.Request(f'{domain}/meme')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    req.add_header('tags', 'fun')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert len(response) == 1


def test_create_meme(domain):
    """A dummy docstring."""
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
        "text": "Varvara meme",
        "url": "url.com"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == 'Varvara meme'


def test_update_meme(domain):
    """A dummy docstring."""
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
        "text": "Varvara meme updated",
        "url": "url.com",
        "id": 9
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    print(response)
    assert response['text'] == 'Varvara meme updated'


# def test_meme_to_delete(domain):
#     req = request.Request(f'{domain}/meme', method='POST')
#     req.add_header('Content-Type', 'application/json')
#     req.add_header('Authorization', '255a5I8vj9gKF5Z')
#     req.data = json.dumps({
#         "info": {
#             "purpose": "delete",
#             "type": "text"
#             },
#         "tags": [
#             "meme",
#             1111
#         ],
#         "text": "Varvara meme to delete",
#         "url": "url.com"
#     }).encode('ascii')
#     response = request.urlopen(req).read().decode('utf-8')
#     response = json.loads(response)
#     print(response)
#     assert response['text'] == 'Varvara meme to delete'


def test_delete_meme(domain):
    """A dummy docstring."""
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
        "text": "Varvara meme to delete",
        "url": "url.com"
    }).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    meme_id = response["id"]
    req = request.Request(f'{domain}/meme/{meme_id}', method='DELETE')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    response = request.urlopen(req)
    print(response)
    req = request.Request(f'{domain}/meme/{meme_id}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', '255a5I8vj9gKF5Z')
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print(err)
        assert err.code == 404
        return
    assert False
