import json

import pytest
import requests

DOMAIN = 'http://167.172.172.115:52353'


@pytest.fixture(scope='session')
def domain():
    yield DOMAIN

@pytest.fixture(scope='session')
def token(domain):
    url = f'{domain}/authorize'

    payload = json.dumps({
        "name": "Николай Назаров"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    token = response["token"]
    yield token

@pytest.fixture(scope='session')
def token(domain):
    yield

