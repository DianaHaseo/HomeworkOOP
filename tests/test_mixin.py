from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import Lawngrass


class TestProductMixin:
    """Тесты ProductMixin."""

    def test_product_creation_message(self, capsys):
        """Миксин выводит информацию о Product."""
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

    def test_product_repr(self):
        """Проверка __repr__."""
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

    def test_smartphone_creation_message(self, capsys):
        """Миксин работает со Smartphone."""
        Smartphone(
            "Samsung",
            "256GB",
            100000,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )

        captured = capsys.readouterr()

        assert (
            "Создан объект класса Smartphone"
            in captured.out
        )

    def test_lawngrass_creation_message(self, capsys):
        """Миксин работает с Lawngrass."""
        Lawngrass(
            "Газонная трава",
            "Элитная",
            500,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        captured = capsys.readouterr()

        assert (
            "Создан объект класса Lawngrass"
            in captured.out
        )