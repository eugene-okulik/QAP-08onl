import math
from datetime import datetime
import pytest


@pytest.fixture(scope='session')
def print_text():
    print('\nСейчас будет много тестов)\n')
    yield None
    print('\nСпасибо за внимание!\n')


@pytest.fixture(scope='function')
def next_text():
    print('\nЭта нанало теста.\n')
    yield None
    print('\nА вот это конец.\n')


@pytest.mark.usefixtures
@pytest.mark.simple
def test_sum():
    assert 5+5 == 10, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
@pytest.mark.parametrize('result', [3, 2, 11, 5, 25])
def test_diff(result):
    assert 5-2 == result, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
def test_product():
    assert 5*3 == 15, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
def test_quotient():
    assert 20/2 == 10, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
def test_equation():
    assert 20/2+5 == 15, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
def test_less():
    assert 9 < 11, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
@pytest.mark.skip('Bag - #325')
def test_more():
    assert 7 > 5, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
@pytest.mark.skipif(datetime.now().month == 8, reason='в Августе корень не извлекаем')
def test_sqrt():
    assert math.sqrt(9) == 3, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
def test_sqr():
    assert 5 ** 2 == 25, 'Результат не соответствует ожидаемому'


@pytest.mark.usefixtures
@pytest.mark.hard
def test_divide_without_a_remainder():
    assert 1254 % 10 == 4, 'Результат не соответствует ожидаемому'
