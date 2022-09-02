import pytest

DOMAIN = 'http://167.172.172.115:52353'


@pytest.fixture(scope='function')
def domain():
    yield DOMAIN
