import pytest


@pytest.mark.usefixtures('set_up', 'action')
class TestSimple:
    @pytest.mark.skip('Test is too simple')
    def test1(self):
        assert 1 + 5 == 6

    @pytest.mark.simple
    def test2(self):
        assert 5 - 2 == 6, "Фактический результат не соответствует ожидаемомоу"

    @pytest.mark.simple
    @pytest.mark.parametrize('x_1,y_1', [[9, 7], [11, 2]])
    def test3(self, x_1, y_1):
        assert x_1 > y_1, "Фактический результат не соответствует ожидаемомоу"

    @pytest.mark.simple
    def test4(self):
        assert 3 + 3 == 6

    @pytest.mark.simple
    def test5(self):
        assert 4 - 1 == 3

    @pytest.mark.simple
    def test6(self):
        assert 4 / 2 == 2

    @pytest.mark.simple
    def test7(self):
        assert 4 + 5 == 9

    @pytest.mark.simple
    def test8(self):
        assert 5+5 == 10

    @pytest.mark.simple
    def test9(self):
        assert 1+1 == 2

    @pytest.mark.simple
    def test10(self):
        res11 = 10 + 20
        assert res11 == 30
