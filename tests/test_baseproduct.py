import pytest

from src.baseproduct import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import Lawngrass


def test_base_product_is_abstract():
    """BaseProduct является абстрактным классом."""
    assert BaseProduct.__abstractmethods__


def test_base_product_cannot_be_created():
    """Нельзя создать экземпляр абстрактного класса."""
    with pytest.raises(TypeError):
        BaseProduct(
            "Тест",
            "Описание",
            100.0,
            10
        )


def test_product_inherits_base_product():
    """Product наследуется от BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_product_is_instance_of_base_product():
    """Экземпляр Product является BaseProduct."""
    product = Product(
        "Тест",
        "Описание",
        100.0,
        10
    )

    assert isinstance(product, BaseProduct)


def test_smartphone_inherits_only_product():
    """Smartphone напрямую наследуется только от Product."""
    assert Smartphone.__bases__ == (Product,)


def test_lawngrass_inherits_only_product():
    """Lawngrass напрямую наследуется только от Product."""
    assert Lawngrass.__bases__ == (Product,)