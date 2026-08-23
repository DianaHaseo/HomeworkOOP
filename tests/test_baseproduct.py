from src.baseproduct import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import Lawngrass


def test_base_product_is_abstract():
    """BaseProduct является абстрактным классом."""
    assert BaseProduct.__abstractmethods__


def test_product_inherits_base_product():
    """Product наследует BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_product_is_instance_of_base_product():
    """Экземпляр Product является BaseProduct."""
    product = Product(
        "Тест",
        "Описание",
        100,
        10
    )

    assert isinstance(product, BaseProduct)


def test_smartphone_inherits_only_product():
    """Smartphone напрямую наследует только Product."""
    assert Smartphone.__bases__ == (Product,)


def test_lawngrass_inherits_only_product():
    """Lawngrass напрямую наследует только Product."""
    assert Lawngrass.__bases__ == (Product,)