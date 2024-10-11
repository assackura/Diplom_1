import pytest

from data import DataBuns, DataIng


class TestDataBase:

    @pytest.mark.parametrize(DataBuns.parametrs, DataBuns.values)
    def test_available_buns(self, db, name, price):
        list_names = []
        list_prices = []
        for bun_name in db.available_buns():
            list_names.append(bun_name.get_name())
            list_prices.append(bun_name.get_price())

        assert name in list_names and price in list_prices

    @pytest.mark.parametrize(DataIng.parametrs, DataIng.values)
    def test_available_ingredients(self, db, type_ing, name, price):
        list_names = []
        list_prices = []
        list_types = []
        for ing in db.available_ingredients():
            list_types.append(ing.get_type())
            list_prices.append(ing.get_price())
            list_names.append(ing.get_name())

        assert name in list_names and price in list_prices and type_ing in list_types