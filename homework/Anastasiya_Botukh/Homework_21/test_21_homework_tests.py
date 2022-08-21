import pytest


def test_sum(every_session, some_sessions):
    print('sum')
    assert 1 + 1 == 2, 'Wrong result'


@pytest.mark.simple
def test_sum_1(every_session):
    print('sum_1')
    assert 2 + 2 == 4, 'Wrong result'


def test_sum_2(every_session):
    print('sum_2')
    assert 3 + 3 == 6, 'Wrong result'


def test_dif(every_session, some_sessions):
    print('dif')
    assert 3 - 1 == 2, 'Wrong result'


def test_dif_1(every_session):
    print('dif_1')
    assert 5 - 4 == 1, 'Wrong result'


@pytest.mark.hard
def test_dif_2(every_session):
    print('dif_2')
    assert 10 - 1 == 9, 'Wrong result'


@pytest.mark.parametrize('a, b', [[10, 2], [4, 1], [8, 8]])
def test_sum_3(every_session, some_sessions, a, b):
    print('sum')
    result = a + b
    assert a+b == result, 'not right result'


@pytest.mark.skip(reason='bug - #1')
@pytest.mark.parametrize('a', [17, 9, 8])
def test_diff_3(every_session, a):
    print('diff')
    assert 17-9 == a, 'not right result'


def test_9(every_session, some_sessions):
    assert 21 * 16 == 336, 'Wrong result'


@pytest.mark.skip(reason='bug - #2')
def test_10(every_session):
    assert 10 / 5 == 5, 'Wrong result'
