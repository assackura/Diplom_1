import pytest

from data import OtherData, DataIng
from unittest.mock import Mock


class TestBurger:

    def test_burger_set_buns(self, burger):
        assert burger.bun is not None

    def test_add_ingredient(self, burger):
        assert burger.ingredients != []

    def test_remove_ingredient(self, burger):
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, burger):
        burger.move_ingredient(OtherData.MOVE_ING_DATA[0],  OtherData.MOVE_ING_DATA[1])

        assert burger.ingredients[OtherData.MOVE_ING_DATA[1]].get_name() == OtherData.MOVE_ING_DATA[2]

    def test_get_price_burger(self, burger):
        assert burger.get_price() == OtherData.FINAL_PRICE_BURGER

    def test_get_receipt(self, burger):
        assert burger.get_receipt() == OtherData.EXPECTED_TICKET
