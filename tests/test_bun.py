import pytest
from data import DataBuns
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(DataBuns.parametrs, DataBuns.values)
    def test_get_name_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(DataBuns.parametrs, DataBuns.values)
    def test_get_price_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
