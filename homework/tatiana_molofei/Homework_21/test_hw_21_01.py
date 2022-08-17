import math
import pytest


@pytest.fixture(scope='session',  name='print_begin_end')
def print_text():
    print("\nBefore first test\n")
    yield None
    print("\nAfter last test\n")


@pytest.fixture(scope='function', name='print_all')
def print_all_tests():
    print("\nBefore every test\n")
    yield None
    print("\nAfter every test\n")


@pytest.mark.simple
def test_sum(print_begin_end, print_all):
    assert 2+2 == 4


@pytest.mark.simple
def test_dif(print_all):
    assert 5-2 == 3


@pytest.mark.simple
def test_mult(print_all):
    assert 4*3 == 12


@pytest.mark.hard
def test_div(print_all):
    assert 4 / 2 == 2


@pytest.mark.simple
def test_isalpha(print_all):
    assert "helloMyFriend".isalpha()


@pytest.mark.hard
def test_isdigit(print_all):
    assert "34566".isdigit()


@pytest.mark.hard
@pytest.mark.skip("Useless test")
def test_entry(print_all):
    assert 'a' in "Tryam"


@pytest.mark.hard
def test_comp(print_all):
    assert 6 < 8


@pytest.mark.hard
def test_pow(print_all):
    assert 2 ** 4 == 16


@pytest.mark.hard
def test_round(print_all):
    assert math.ceil(8.999) == 9


@pytest.mark.hard
@pytest.mark.parametrize('items', [5, 7])
def test_factorial(print_all, items):
    result = math.factorial(items)
    assert result == 120
