"""System module."""
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

import pytest


@pytest.fixture(scope='session')
def print_session_text():
    """A dummy docstring."""
    print('\nSession Starts\n')
    yield None
    print('\nSession Ends\n')


@pytest.fixture(scope='function')
def print_text(request):
    """A dummy docstring."""
    print(f"BEFORE {request.function.__name__}")
    yield None
    print(f"AFTER {request.function.__name__}")


def test_sum1(print_session_text, print_text):
    """A dummy docstring."""
    print("sum")
    assert 2 + 2 == 4, 'Результат не соответствует ожидаемому'


def test_sum2(print_text):
    """A dummy docstring."""
    assert 5 + 2 == 7, 'Результат не соответствует ожидаемому'


def test_sum3(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


def test_sum4(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


def test_sum5(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


def test_sum6(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


@pytest.mark.parametrize('one, two', [[1, 2], [3, 4], [5, 6]])
def test_sum7(print_text, one, two):
    """A dummy docstring."""
    result = one + two
    assert one + two == result, 'Результат не соответствует ожидаемому'


@pytest.mark.hard
def test_sum8(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_sum9(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'


@pytest.mark.skip('bug')
def test_sum10(print_text):
    """A dummy docstring."""
    assert 3 + 3 == 6, 'Результат не соответствует ожидаемому'
