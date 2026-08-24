from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import Lawngrass


def test_product_mixin_prints_creation_info(capsys):
    """Миксин выводит информацию при создании Product."""
    Product(
        "Продукт1",
        "Описание продукта",
        1200,
        10
    )

    captured = capsys.readouterr()

    assert "Создан объект класса Product" in captured.out
    assert "Продукт1" in captured.out
    assert "Описание продукта" in captured.out
    assert "1200" in captured.out
    assert "10" in captured.out


def test_product_mixin_prints_smartphone_info(capsys):
    """Миксин работает при создании Smartphone."""
    Smartphone(
        "Samsung Galaxy S23",
        "256GB, Серый",
        180000.0,
        5,
        95.5,
        "S23",
        256,
        "Серый"
    )

    captured = capsys.readouterr()

    assert "Создан объект класса Smartphone" in captured.out
    assert "Samsung Galaxy S23" in captured.out


def test_product_mixin_prints_lawngrass_info(capsys):
    """Миксин работает при создании Lawngrass."""
    Lawngrass(
        "Газонная трава",
        "Элитная трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    captured = capsys.readouterr()

    assert "Создан объект класса Lawngrass" in captured.out
    assert "Газонная трава" in captured.out


def test_product_repr():
    """Проверяется __repr__ Product."""
    product = Product(
        "Продукт1",
        "Описание продукта",
        1200,
        10
    )

    assert repr(product) == (
        "Product("
        "'Продукт1', "
        "'Описание продукта', "
        "1200, "
        "10)"
    )


def test_smartphone_repr():
    """Проверяется наследование __repr__ Smartphone."""
    smartphone = Smartphone(
        "Samsung Galaxy S23",
        "256GB, Серый",
        180000.0,
        5,
        95.5,
        "S23",
        256,
        "Серый"
    )

    assert repr(smartphone).startswith("Smartphone(")


def test_lawngrass_repr():
    """Проверяется наследование __repr__ Lawngrass."""
    lawngrass = Lawngrass(
        "Газонная трава",
        "Элитная трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    assert repr(lawngrass).startswith("Lawngrass(")