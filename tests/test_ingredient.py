import pytest

from data import DataIng
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(DataIng.parametrs, DataIng.values)
    def test_get_price_ingredient(self, type_ing, name, price):
        ing = Ingredient(type_ing, name, price)
        assert ing.get_price() == price

    @pytest.mark.parametrize(DataIng.parametrs, DataIng.values)
    def test_get_name_ingredient(self, type_ing, name, price):
        ing = Ingredient(type_ing, name, price)
        assert ing.get_name() == name

    @pytest.mark.parametrize(DataIng.parametrs, DataIng.values)
    def test_get_type_ingredient(self, type_ing, name, price):
        ing = Ingredient(type_ing, name, price)
        assert ing.get_type() == type_ing