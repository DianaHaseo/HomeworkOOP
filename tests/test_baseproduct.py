import pytest

from src.baseproduct import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import Lawngrass


class TestBaseProduct:

    def test_base_product_is_abstract(self):
        """BaseProduct является абстрактным классом."""

        assert BaseProduct.__abstractmethods__

    def test_base_product_cannot_be_created(self):
        """Нельзя создать объект BaseProduct."""

        with pytest.raises(TypeError):
            BaseProduct(
                "Тест",
                "Описание",
                100.0,
                10
            )

    def test_product_inherits_base_product(self):
        """Product наследуется от BaseProduct."""

        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_product(self):
        """Smartphone наследуется от Product."""

        assert Smartphone.__bases__ == (Product,)

    def test_lawngrass_inherits_product(self):
        """Lawngrass наследуется от Product."""

        assert Lawngrass.__bases__ == (Product,)