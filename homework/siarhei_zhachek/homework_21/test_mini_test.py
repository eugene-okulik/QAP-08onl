import pytest
import math
from datetime import datetime


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


@pytest.mark.simple
def test_sum(print_text, next_text):
    assert 5+5 == 10, 'Результат не соответствует ожидаемому'


@pytest.mark.parametrize('result', [3, 2, 11, 5, 25])
def test_diff(result, next_text, print_text):
    assert 5-2 == result, 'Результат не соответствует ожидаемому'


def test_product(print_text, next_text):
    assert 5*3 == 15, 'Результат не соответствует ожидаемому'


def test_quotient(print_text, next_text):
    assert 20/2 == 10, 'Результат не соответствует ожидаемому'


def test_text(print_text, next_text):
    assert 'abc' == 'abc', 'Результат не соответствует ожидаемому'


def test_less(print_text, next_text):
    assert 9 < 11, 'Результат не соответствует ожидаемому'


@pytest.mark.skip('Bag - #325')
def test_more(print_text, next_text):
    assert 7 > 5, 'Результат не соответствует ожидаемому'


@pytest.mark.skipif(datetime.now().month == 8, reason='в Августе корень не извлекаем')
def test_sqrt(print_text, next_text):
    assert math.sqrt(9) == 3, 'Результат не соответствует ожидаемому'


def test_sqr(print_text, next_text):
    assert 5 ** 2 == 25, 'Результат не соответствует ожидаемому'


@pytest.mark.hard
def test_divide_without_a_remainder(print_text, next_text):
    assert 1254 % 10 == 4, 'Результат не соответствует ожидаемому'
