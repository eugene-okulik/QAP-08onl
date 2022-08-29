import pytest


@pytest.fixture(scope='session')
def print_session_text():
    print('\nTesting loading...\n')
    yield None
    print('\nEnd\n')


@pytest.fixture(scope='function')
def print_text():
    print('\nНачало проверки теста\n')
    yield None
    print('\nКонец проверки теста\n')


# pylint: disable=unused-argument, no-self-use
# pylint: disable=redefined-outer-name
def test_1(print_session_text, print_text):
    print("Ниже примеры суммы, вычитания, умножения, деления")
    assert 5 + 3 == 8, 'Результат не соответствует ожидаемому'


def test_2(print_text):
    assert 7 - 2 == 5, 'Результат не соответствует ожидаемому'


def test_3(print_text):
    assert 2 * 3 == 6, 'Результат не соответствует ожидаемому'


def test_4(print_text):
    assert 4 // 2 == 2, 'Результат не соответствует ожидаемому'


def test_5(print_text):
    assert 6 // 3 == 2, 'Результат не соответствует ожидаемому'


def test_6(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_7(print_text):
    assert 5 - 5 == 0, 'Результат не соответствует ожидаемому'


@pytest.mark.parametrize('x_num, y_num', [[3, 4], [4, 5], [5, 6]])
def test_8(print_text, x_num, y_num):
    result = x_num + y_num
    assert x_num + y_num == result, 'Результат не соответствует ожидаемому'


@pytest.mark.skip('Bug 343')
def test_9(print_text):
    assert 9 * 2 == 18, 'Результат не соответствует ожидаемому'


@pytest.mark.hard
def test_10(print_text):
    assert 10 - 6 == 4, 'Результат не соответствует ожидаемому'
