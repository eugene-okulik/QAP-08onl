import pytest


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.skip('Test is too simple')
def test1():
    assert 1 + 5 == 6


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test2():
    assert 5 - 2 == 6, "Фактический результат не соответствует ожидаемомоу"


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
@pytest.mark.parametrize('x_1,y_1', [[9, 7], [11, 2]])
def test3(x_1, y_1):
    assert x_1 > y_1, "Фактический результат не соответствует ожидаемомоу"


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test4():
    assert 3 + 3 == 6


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test5():
    assert 4 - 1 == 3


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test6():
    assert 4 / 2 == 2


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test7():
    assert 4 + 5 == 9


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test8():
    assert 5+5 == 10


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test9():
    assert 1+1 == 2


@pytest.mark.usefixtures('set_up', 'action')
@pytest.mark.simple
def test10():
    res11 = 10 + 20
    assert res11 == 30
