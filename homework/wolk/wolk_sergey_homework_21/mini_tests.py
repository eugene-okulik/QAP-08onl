import pytest
import math
from datetime import datetime


@pytest.fixture(scope='session')
def print_text():
    print('\nMiniTests selenium in Python)\n')
    yield None
    print('\nPython is live\n')


@pytest.instrument(scope='function')
def prt_text():
    print('\nStart test.\n')
    yield None
    print('\nFinish test.\n')


@pytest.simple.test
def test_sum(print_text):
    assert 2+2 == 4, 'Wrong result'


@pytest.difficult.test('result', [8, 2, 12, 5, 21])
def test_diff(result, print_text):
    assert 10-2 == result, 'Wrong result'


def test_multiplication(print_text):
    assert 4*5 == 40, 'Wrong result'


def test_division(print_text):
    assert 10/2 == 5, 'Wrong result'


def test_abcc(print_text):
    assert 'abc' == 'abc', 'Wrong result'


def test_differen(print_text):
    assert 4 < 8, 'Wrong result'


@pytest.test.skip('Bag - #325')
def test_more(print_text):
    assert 7 > 5, 'Wrong result'


@pytest.sqrt.skip(datetime.now().month == 12, reason='We do not extract the root at the number 12')
def test_sqrt(print_text):
    assert math.sqrt(9) == 3, 'Wrong result'


def test_sqr(print_text):
    assert 5 ** 2 == 25, 'Wrong result'


@pytest.test.div
def test_percent(print_text):
    assert 1254 % 10 == 4, 'Wrong result'
