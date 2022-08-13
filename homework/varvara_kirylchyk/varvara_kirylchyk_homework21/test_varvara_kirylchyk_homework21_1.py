# Pytest
#
# Создайте 10 тестов, которые проверяют сами себя
# (бессмысленные тесты, которые делали на занятии,
# типа assert 2+2 == 4)
# Добавьте действие, которое отрабатывает перед всем запуском тестов,
# а также после окончания тестирования
# Добавьте действие, которое отрабатывает до и после каждого теста
# Сделайте возможным запуск тестов помеченных как “simple” и “hard”
# Пропустите выполнение одного теста и пометьте причину пропуска
# Хотя бы один тест должен работать с набором тестовых данных

import pytest as pytest


@pytest.fixture(scope='session')
def print_session_text():
    print('\nbefore session1\n')
    yield None
    print('\nafter session2\n')


@pytest.fixture(scope='function')
def print_text():
    print('\nbefore test1\n')
    yield None
    print('\nafter test2\n')


def test_sum1(print_session_text, print_text):
    print("sum")
    assert 2 + 2 == 4, 'Результат не соответствует ожидаемому'


def test_sum2(print_text):
    assert 5 + 2 == 7, 'Результат не соответствует ожидаемому'


def test_sum3(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


def test_sum4(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


def test_sum5(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


def test_sum6(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'

@pytest.mark.parametrize('a, b', [[1,2],[3,4],[5,6]])
def test_sum7(print_text, a, b):
    result = a + b
    assert a + b == result, 'Результат не соответствует ожидаемому'

@pytest.mark.hard
def test_sum8(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'

@pytest.mark.simple
def test_sum9(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'

@pytest.mark.skip('bug')
def test_sum10(print_text):
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'
