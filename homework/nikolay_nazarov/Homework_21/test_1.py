import pytest


@pytest.fixture(scope='function')
def every_func():
    print('\nevery_func_fixture - before')
    yield None
    print('\nevery_func_fixture - after')


@pytest.fixture(scope='session')
def every_session():
    print('\nevery_session_fixture - before session')
    yield None
    print('every_session_fixture - after session')


@pytest.mark.hard("Тяжелый тест")
def test_1(every_session, every_func):
    print('test_1 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.simple("Легкий тест")
def test_2(every_session_fixture, every_func_fixture):
    print('test_2 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.skip(reason="bug 295")
def test_3(every_session_fixture, every_func_fixture):
    print('test_3 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.parametrize("a, b", [[1, 2], [1, 3], [4, 2], [5, 3]])
def test_4(a, b, every_session_fixture, every_func_fixture):
    print('test_4 - inside')
    result = a + b
    assert a + b == result, "2+2 не равно 4"


def test_5(every_session_fixture, every_func_fixture):
    print('test_5 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


def test_6(every_session_fixture, every_func_fixture):
    print('test_6 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


def test_7(every_session_fixture, every_func_fixture):
    print('test_7 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


def test_8(every_session_fixture, every_func_fixture):
    print('test_8 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


def test_9(every_session_fixture, every_func_fixture):
    print('test_9 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


def test_10(every_session_fixture, every_func_fixture):
    print('test_10 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"
