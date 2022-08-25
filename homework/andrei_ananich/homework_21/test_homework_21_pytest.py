"""module"""
import pytest


@pytest.fixture(scope='session')
def test_print_all_text():
    """module"""
    print('\nbefore all test\n')
    yield None
    print('\nafter all test\n')


@pytest.fixture(scope='function')
def test_print_text():
    """module"""
    print('\nbefore test\n')
    yield None
    print('\nafter test')


def test_all():
    """module"""
    print('test_all')
    assert 2+2+2+2+2 == 10, 'Результат не соответсвует ожидаемому'
    return test_print_all_text, test_print_text


def test_sum2():
    """module"""
    print('sum2')
    assert -2+3 == 1, 'Результат не соответсвует ожидаемому'
    return test_print_text


def test_minus():
    """module"""
    print('minus')
    assert 3-2 == 1, 'Результат не соответсвует ожидаемому'
    return test_print_text


def test_minus2():
    """module"""
    print('minus2')
    assert 2-3 == -1, 'Результат не соответсвует ожидаемому'
    return test_print_text


def test_multiply():
    """module"""
    print('multiply')
    assert 3*2 == 6, 'Результат не соответсвует ожидаемому'
    return test_print_text


def test_multiply2():
    """module"""
    print('multiply2')
    assert 3*0 == 0, 'Результат не соответсвует ожидаемому'
    return test_print_text


def test_division():
    """module"""
    print('division')
    assert 4/2 == 2, 'Результат не соответсвует ожидаемому'
    return test_print_text


@pytest.mark.simple('1 action')
def test_division2():
    """module"""
    print('division2')
    assert -2/2 == -1, 'Результат не соответсвует ожидаемому'
    return test_print_text


@pytest.mark.hard('2 actions')
def test_multiply_sum():
    """module"""
    print('multiply_sum')
    assert 2+2*2 == 6, 'Результат не соответсвует ожидаемому'
    return test_print_text


@pytest.mark.skip(reason='do not need')
def test_multiply_sum2():
    """module"""
    print('multiply_sum2')
    assert (2+2)*2 == 8, 'Результат не соответсвует ожидаемому'
    return test_print_text


@pytest.mark.parametrize('a_type, b_type', [[2, 2], [3, 3], [4, 4]])
def test_sum(a_type, b_type):
    """module"""
    print('sum')
    result = a_type + b_type
    assert a_type+b_type == result, 'Результат не соответсвует ожидаемому'
