import pytest

@pytest.fixture(scope='function')
def print_text():
    print('\nbefore test\n')
    yield None
    print('\nfter test')

@pytest.mark.parametrize('a, b', [[]])
def test_sum(a, b):
    print('sum')
    result = a + b
    assert 2+2 == 4, 'результат не соответствует ожидаемому'

def test_diff():
    print('diff')
    assert 3-2 == 1, 'результат не соответствует ожидаемому'
