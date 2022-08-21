import pytest


@pytest.fixture(scope='session')
def print_session_text():
    print('\nTest start\n')
    yield None
    print('\nEnd\n')


@pytest.fixture(scope='function')
def print_text():
    print('\nНачало теста\n')
    yield None
    print('\nКонец теста\n')


@pytest.mark.simple
def test_1(print_text):
    assert 3 + 5 == 8, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_2(print_text):
    assert 6 - 2 == 4, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_3(print_text):
    assert 3 * 2 == 6, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_4(print_text):
    assert 8 // 4 == 2, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_5(print_text):
    assert 9 // 3 == 3, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_6(print_text):
    assert 4 + 4 == 8, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_7(print_text):
    assert 2 - 2 == 0, 'Результат не соответствует ожидаемому'


@pytest.mark.hard
@pytest.mark.parametrize('x_num, z_num', [[2, 3], [3, 4], [4, 5]])
def test_8(print_text, x_num, z_num):
    result = x_num + z_num
    assert x_num + z_num == result, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
@pytest.mark.skip('Bug №400')
def test_9(print_text):
    assert 6 * 2 == 12, 'Результат не соответствует ожидаемому'


@pytest.mark.simple
def test_10(print_text):
    assert 9 - 2 == 7, 'Результат не соответствует ожидаемому'
