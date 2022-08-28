import pytest


@pytest.mark.usefixtures
@pytest.mark.hard("Тяжелый тест")
def test_1():
    print('test_1 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
@pytest.mark.simple("Легкий тест")
def test_2():
    print('test_2 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
@pytest.mark.skip(reason="bug 295")
def test_3():
    print('test_3 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
@pytest.mark.parametrize("first_number, second_number", [[1, 2], [1, 3], [4, 2], [5, 3]])
def test_4(first_number, second_number):
    print('test_4 - inside')
    result = first_number + second_number
    assert first_number + second_number == result, "2+2 не равно 4"


@pytest.mark.usefixtures
def test_5():
    print('test_5 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
def test_6():
    print('test_6 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
def test_7():
    print('test_7 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
def test_8():
    print('test_8 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
def test_9():
    print('test_9 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"


@pytest.mark.usefixtures
def test_10():
    print('test_10 - inside')
    assert 2 + 2 == 4, "2+2 не равно 4"
