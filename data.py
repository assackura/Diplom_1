from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class DataBuns:
    parametrs = 'name, price'
    values = [
        ['black bun', 100],
        ['white bun', 200],
        ['red bun', 300]
    ]
    DATA_MOCK_BUNS = ['test bun', 1000]

class DataIng:
    parametrs = 'type_ing, name, price'
    values = [
        [INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [INGREDIENT_TYPE_FILLING, 'sausage', 300]
    ]
    DATA_MOCK_ING_SAUCE = [INGREDIENT_TYPE_SAUCE, 'test sauce', 1000]
    DATA_MOCK_ING_FILLING = [INGREDIENT_TYPE_FILLING, 'test filling', 500]

class OtherData:
    MOVE_ING_DATA = [0, 1, "test sauce"] #Данные для теста test_move_ingredient
    FINAL_PRICE_BURGER = 3500
    EXPECTED_TICKET = '\n'.join([
        f"(==== {DataBuns.DATA_MOCK_BUNS[0]} ====)",
        f"= {DataIng.DATA_MOCK_ING_SAUCE[0].lower()} {DataIng.DATA_MOCK_ING_SAUCE[1]} =",
        f"= {DataIng.DATA_MOCK_ING_FILLING[0].lower()} {DataIng.DATA_MOCK_ING_FILLING[1]} =",
        f"(==== {DataBuns.DATA_MOCK_BUNS[0]} ====)\n",
        f"Price: {FINAL_PRICE_BURGER}"
        ])