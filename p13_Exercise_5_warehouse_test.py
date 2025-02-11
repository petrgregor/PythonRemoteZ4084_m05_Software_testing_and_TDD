import pytest

from p13_Exercise_5_warehouse import Product, Warehouse


params_product = [
    ("product 1", 2.75, True),
    ("product 2", "3", False),
    ("product 3", -5, False)
]


@pytest.mark.parametrize("name, volume, result", params_product)
def test_product_init(name, volume, result):
    if result:
        assert Product(name, volume).__repr__() == f"Product(name={name}, volume={volume})"
    elif isinstance(volume, str):
        with pytest.raises(TypeError):
            Product(name, volume)
    elif isinstance(volume, (int, float)) and volume < 0:
        with pytest.raises(ValueError):
            Product(name, volume)


params_warehouse = [
    (50, True),
    (5.15, True),
    (0, ValueError),
    (-50, ValueError),
    ("30", TypeError)
]


@pytest.mark.parametrize("capacity, result", params_warehouse)
def test_warehouse_init(capacity, result):
    if isinstance(result, bool) and result:
        assert Warehouse(capacity).__repr__() == f"Warehouse(capacity={capacity}, products=0)"
    else:
        with pytest.raises(result):
            Warehouse(capacity)


@pytest.fixture
def products():
    return [
        Product("Item 1", 13.75),
        Product("Item 2", 2.15),
        Product("Item 3", 30)
    ]


params_warehouse_capacity = [
    (40, -1),
    (50, 4.1),
    (67.35, 21.45)
]


@pytest.mark.parametrize("capacity, result", params_warehouse_capacity)
def test_warehouse_add(products, capacity, result):
    warehouse = Warehouse(capacity)
    return_value = None
    for product in products:
        return_value = warehouse.add(product)

    assert round(return_value, 2) == result
