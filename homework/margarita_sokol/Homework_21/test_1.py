# Создайте 10 тестов, которые проверяют сами себя (бессмысленные тесты,
# которые делали на занятии, типа assert 2+2 == 4)
# Добавьте действие, которое отрабатывает перед всем запуском тестов,
# а также после окончания тестирования
# Добавьте действие, которое отрабатывает до и после каждого теста
# Сделайте возможным запуск тестов помеченных как “simple” и “hard”
# Пропустите выполнение одного теста и пометьте причину пропуска
# Хотя бы один тест должен работать с набором тестовых данных

import pytest


@pytest.fixture(scope='session')
def _print_session_text():
    print('\nSession Starts\n')
    yield None
    print('\nSession Ends\n')


@pytest.fixture(scope='function')
def _print_text():
    print('\nНачало проверки теста\n')
    yield None
    print('\nКонец проверки теста\n')


@pytest.mark.parametrize('num1, num2', [[2, 3], [4, 5], [6, 7]])
def test_1(_print_text, num1, num2):
    result = num1 + num2
    assert num1 + num2 == result, 'Результат не соответствует ожидаемому'


def test_2(_print_session_text, _print_text):
    print('sum')
    assert 5 + 4 == 9, 'Результат не соответствует ожидаемому'


def test_3(_print_text):
    assert 5 * 5 == 25, 'Результат не соответствует ожидаемому'


@pytest.mark.skip('bug 111')
def test_4(_print_text):
    assert 8 // 2 == 4, 'Результат не соответствует ожидаемому'


def test_5(_print_text):
    assert 5 * 3 == 15, 'Результат не соответствует ожидаемому'


def test_6(_print_text):
    assert 9 - 7 == 2, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_7(_print_text):
    assert 5 + 1 == 6, 'Результат не соответствует ожидаемому'


def test_8(_print_text):
    assert 5 ** 2 == 25, 'Результат не соответствует ожидаемому'


@pytest.mark.hard
def test_9(_print_text):
    assert 9 * 17 == 153, 'Результат не соответствует ожидаемому'


def test_10(_print_text):
    assert 25 - 19 == 6, 'Результат не соответствует ожидаемому'
