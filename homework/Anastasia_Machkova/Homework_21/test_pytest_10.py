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
def test_1(this_test):
    print('test_1')
    assert 2+2 == 4, 'The result is not as expected'


@pytest.mark.simple
def test_2(this_test):
    print('test_2')
    assert 3-1 == 2, 'The result is not as expected'


def test_3(this_test):
    print('test_3')
    assert 11*11 == 121, 'The result is not as expected'


@pytest.mark.skip(reason='Bug #3')
def test_4(this_test):
    print('test_4')
    assert 10/5 == 2, 'The result is not as expected'


@pytest.mark.hard
@pytest.mark.parametrize('x', [3, 4, 5])
def test_5(x, this_test):
    print('test_5')
    assert 15/3 == x, 'The result is not as expected'


@pytest.mark.hard
@pytest.mark.parametrize('a, b', [[1, 2], [3, 4], [5, 6]])
def test_6(a, b, this_test):
    print('test_6')
    result = a + b
    assert a+b == result, 'The result is not as expected'


@pytest.mark.simple
def test_7(this_test):
    print('test_7')
    assert 4*4 == 15, 'The result is not as expected'


@pytest.mark.parametrize('x', [56])
def test_8(x, this_test):
    print('test_8')
    assert 7*8 == x, 'The result is not as expected'


def test_9(this_test):
    print('test_9')
    assert 100/2 == 50, 'The result is not as expected'


def test_10(this_test):
    print('test_10')
    assert 5+5 == 11, 'The result is not as expected'
