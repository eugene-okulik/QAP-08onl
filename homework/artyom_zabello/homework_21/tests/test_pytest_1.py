from random import choice, randint
import pytest


@pytest.mark.skip('Test is too simple')
def test1(set_up, action):
    print("1")
    assert True


@pytest.mark.simple
def test2(set_up, action, x_x=randint(1, 7), y_y=randint(1, 20)):
    res = x_x + y_y
    assert res <= 25


@pytest.mark.simple
@pytest.mark.parametrize('x,y', [[5, 7], [11, 2], [14, 6]])
def test3(set_up, action, x, y):
    res = x + y
    assert res <= 15


@pytest.mark.simple
def test4(set_up, action, x=1, y=5):
    print(f"x+y ={x + y}")
    assert "x+y =6"


@pytest.mark.simple
def test5(set_up, action):
    print(1)
    assert 1


@pytest.mark.simple
def test6(set_up, action, x=randint(1, 50)):
    if x < 49:
        res = True
    else:
        res = False
    assert res


@pytest.mark.simple
def test7(set_up, action, x=choice(['One', 'Two'])):
    if x is 'One':
        res = True
    else:
        res = False
    assert res


@pytest.mark.simple
def test8(set_up, action, x=choice([5, 6])):
    if x is 6:
        res = True
    else:
        res = False
    assert res


@pytest.mark.simple
def test9(set_up, action, re_x=choice([True, False])):
    if re_x:
        print('Test')
    assert 'Test'


@pytest.mark.simple
def test10(set_up, action):
    res11 = 10 + 20
    assert res11 == 30
