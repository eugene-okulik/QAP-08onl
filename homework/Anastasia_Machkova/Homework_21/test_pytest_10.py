import pytest


@pytest.fixture(scope='function')
def this_test():
    print('\nReady to test\n')
    yield
    print('\nI am done with test\n')


@pytest.fixture(scope='session')
def all_tests():
    print('\nNow all tests will run\n')
    yield""
    print('\nTesting is finished\n')


@pytest.mark.simple
@pytest.mark.usefixtures(this_test, all_tests)
def test_1():
    print('test_1')
    assert 2+2 == 4, 'The result is not as expected'


@pytest.mark.simple
@pytest.mark.usefixtures(this_test)
def test_2():
    print('test_2')
    assert 3-1 == 2, 'The result is not as expected'


@pytest.mark.usefixtures(this_test)
def test_3():
    print('test_3')
    assert 11*11 == 121, 'The result is not as expected'


@pytest.mark.skip(reason='Bug #3')
@pytest.mark.usefixtures(this_test)
def test_4():
    print('test_4')
    assert 10/5 == 2, 'The result is not as expected'


@pytest.mark.hard
@pytest.mark.parametrize('x_num', [3, 4, 5])
@pytest.mark.usefixtures(this_test)
def test_5(x_num):
    print('test_5')
    assert 15/3 == x_num, 'The result is not as expected'


@pytest.mark.hard
@pytest.mark.parametrize('a_num, b_num', [[1, 2], [3, 4], [5, 6]])
@pytest.mark.usefixtures(this_test)
def test_6(a_num, b_num):
    print('test_6')
    result = a_num + b_num
    assert a_num+b_num == result, 'The result is not as expected'


@pytest.mark.simple
@pytest.mark.usefixtures(this_test)
def test_7():
    print('test_7')
    assert 4*4 == 15, 'The result is not as expected'


@pytest.mark.parametrize('y_num', [56])
@pytest.mark.usefixtures(this_test)
def test_8(y_num):
    print('test_8')
    assert 7*8 == y_num, 'The result is not as expected'


@pytest.mark.usefixtures(this_test)
def test_9():
    print('test_9')
    assert 100/2 == 50, 'The result is not as expected'


@pytest.mark.usefixtures(this_test)
def test_10():
    print('test_10')
    assert 5+5 == 11, 'The result is not as expected'
