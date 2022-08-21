import pytest


@pytest.mark.usefixtures('every_session', 'some_sessions')
def test_sum():
    print('sum')
    assert 1 + 1 == 2, 'Wrong result'


@pytest.mark.usefixtures('every_session')
@pytest.mark.simple
def test_sum_1():
    print('sum_1')
    assert 2 + 2 == 4, 'Wrong result'


@pytest.mark.usefixtures('every_session')
def test_sum_2():
    print('sum_2')
    assert 3 + 3 == 6, 'Wrong result'


@pytest.mark.usefixtures('every_session', 'some_sessions')
def test_dif():
    print('dif')
    assert 3 - 1 == 2, 'Wrong result'


def test_dif_1(every_session):
    print('dif_1')
    assert 5 - 4 == 1, 'Wrong result'


@pytest.mark.usefixtures('every_session')
@pytest.mark.hard
def test_dif_2():
    print('dif_2')
    assert 10 - 1 == 9, 'Wrong result'


@pytest.mark.usefixtures('every_session', 'some_sessions')
@pytest.mark.parametrize('a, b', [[10, 2], [4, 1], [8, 8]])
def test_sum_3(a_num, b_num):
    print('sum')
    result = a_num + b_num
    assert a_num+b_num == result, 'not right result'


@pytest.mark.usefixtures('every_session')
@pytest.mark.skip(reason='bug - #1')
@pytest.mark.parametrize('a_num', [17, 9, 8])
def test_diff_3(a_num):
    print('diff')
    assert 17-9 == a_num, 'not right result'


@pytest.mark.usefixtures('every_session', 'some_sessions')
def test_9():
    assert 21 * 16 == 336, 'Wrong result'


@pytest.mark.usefixtures('every_session')
@pytest.mark.skip(reason='bug - #2')
def test_10(every_session):
    assert 10 / 5 == 5, 'Wrong result'
