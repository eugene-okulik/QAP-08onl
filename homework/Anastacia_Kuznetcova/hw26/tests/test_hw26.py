import requests
from homework.Anastacia_Kuznetcova.hw26.utils.methods import Util
from homework.Anastacia_Kuznetcova.hw26.utils.json_files import JsonFiles
from homework.Anastacia_Kuznetcova.hw26.utils.methods import ApiMethods

Token = Util.token()


def test_create_meme(domain):
    create_meme_json = JsonFiles.json_create_meme('funny meme',
                                                  'https://memes.com/', 'sarcastic', 'small')
    res: requests.Response = ApiMethods.create_new_meme(domain, create_meme_json, Token)
    assert 'funny meme' in res.json()['text'] and res.status_code == 200


def test_update_meme(domain):
    create_meme_json = JsonFiles.json_create_meme('funny meme',
                                                  'https://memes.com/', 'sarcastic', 'small')
    res_post: requests.Response = ApiMethods.create_new_meme(domain, create_meme_json, Token)
    id_before = res_post.json()['id']
    update_meme_json = JsonFiles.json_update_meme(id_before, 'not funny meme')
    res_put: requests.Response = ApiMethods.update_meme(domain, id_before, update_meme_json, Token)
    assert 'not funny meme' in res_put.json()['text'] and res_put.status_code == 200


def test_del_meme(domain):
    create_meme_json = JsonFiles.json_create_meme('funny meme',
                                                  'https://memes.com/', 'sarcastic', 'small')
    res_post: requests.Response = ApiMethods.create_new_meme(domain, create_meme_json, Token)
    id_before = res_post.json()['id']
    res_delete_meme: requests.Response = ApiMethods.delete_meme(domain, id_before, Token)
    res_get_meme_by_id: requests.Response = ApiMethods.get_meme_by_id(domain, Token, id_before)
    assert f'Meme with id {id_before} successfully deleted' in res_delete_meme.text \
           and res_get_meme_by_id.status_code == 404


def test_get_all_memes(domain):
    res: requests.Response = ApiMethods.get_all_memes(domain, Token)
    res_all_meme = res.json()
    assert len(res_all_meme) == 1


def test_get_tags_memes(domain):
    res: requests.Response = ApiMethods.get_all_memes(domain, Token)
    res_tags_fun = res.json()
    for value in dict(res_tags_fun).values():
        count_tags_fun = 0
        for tags in value:
            for tag in tags["tags"]:
                if tag == 'fun':
                    count_tags_fun += 1
        assert count_tags_fun >= 1
