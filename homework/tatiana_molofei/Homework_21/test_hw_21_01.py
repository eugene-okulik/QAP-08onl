import math
import pytest


@pytest.fixture(scope='session')
def print_text():
    print("\nBefore first test\n")
    yield None
    print("\nAfter last test\n")


@pytest.fixture(scope='function')
def print_all_tests():
    print("\nBefore every test\n")
    yield None
    print("\nAfter every test\n")


@pytest.mark.simple
def test_sum(print_text, print_all_tests):
    assert 2+2 == 4


@pytest.mark.simple
def test_dif(print_all_tests):
    assert 5-2 == 3


@pytest.mark.simple
def test_mult(print_all_tests):
    assert 4*3 == 12


@pytest.mark.hard
def test_div(print_all_tests):
    assert 4 / 2 == 2


@pytest.mark.simple
def test_isalpha(print_all_tests):
    assert "helloMyFriend".isalpha()


@pytest.mark.hard
def test_isdigit(print_all_tests):
    assert "34566".isdigit()


@pytest.mark.hard
@pytest.mark.skip("Useless test")
def test_entry(print_all_tests):
    assert 'a' in "Tryam"


@pytest.mark.hard
def test_comp(print_all_tests):
    assert 6 < 8


@pytest.mark.hard
def test_pow(print_all_tests):
    assert 2 ** 4 == 16


@pytest.mark.hard
def test_round(print_all_tests):
    assert math.ceil(8.999) == 9


@pytest.mark.hard
@pytest.mark.parametrize('items', [5, 7])
def test_factorial(print_all_tests, items):
    result = math.factorial(items)
    assert result == 120
