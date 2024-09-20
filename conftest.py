from unittest.mock import Mock

import pytest
from typing import List

from data import DataBuns, DataIng
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database

@pytest.fixture(scope='function')
def db():
    db = Database()

    return db

@pytest.fixture(scope='function')
def mock_buns():
    mock_buns = Mock()
    mock_buns.name = DataBuns.DATA_MOCK_BUNS[0]
    mock_buns.price = DataBuns.DATA_MOCK_BUNS[1]
    mock_buns.get_name.return_value = DataBuns.DATA_MOCK_BUNS[0]
    mock_buns.get_price.return_value = DataBuns.DATA_MOCK_BUNS[1]

    return mock_buns

@pytest.fixture(scope='function')
def mock_ing_sauce():
    mock_ing = Mock()
    mock_ing.type = DataIng.DATA_MOCK_ING_SAUCE[0]
    mock_ing.name = DataIng.DATA_MOCK_ING_SAUCE[1]
    mock_ing.price = DataIng.DATA_MOCK_ING_SAUCE[2]
    mock_ing.get_type.return_value = DataIng.DATA_MOCK_ING_SAUCE[0]
    mock_ing.get_name.return_value = DataIng.DATA_MOCK_ING_SAUCE[1]
    mock_ing.get_price.return_value = DataIng.DATA_MOCK_ING_SAUCE[2]

    return mock_ing

@pytest.fixture(scope='function')
def mock_ing_filling():
    mock_ing = Mock()
    mock_ing.type = DataIng.DATA_MOCK_ING_FILLING[0]
    mock_ing.name = DataIng.DATA_MOCK_ING_FILLING[1]
    mock_ing.price = DataIng.DATA_MOCK_ING_FILLING[2]
    mock_ing.get_type.return_value = DataIng.DATA_MOCK_ING_FILLING[0]
    mock_ing.get_name.return_value = DataIng.DATA_MOCK_ING_FILLING[1]
    mock_ing.get_price.return_value = DataIng.DATA_MOCK_ING_FILLING[2]

    return mock_ing

@pytest.fixture(scope='function')
def burger(mock_buns, mock_ing_sauce, mock_ing_filling):
    burger = Burger()
    burger.set_buns(mock_buns)
    burger.add_ingredient(mock_ing_sauce)
    burger.add_ingredient(mock_ing_filling)

    return burger



