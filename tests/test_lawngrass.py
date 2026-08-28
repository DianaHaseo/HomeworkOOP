import pytest

from src.product import Product
from src.lawngrass import Lawngrass


class TestLawngrassInit:

    def test_lawngrass_init(self):
        """Создание газонной травы."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        assert lawngrass.name == "Газонная трава"
        assert lawngrass.price == 500.0
        assert lawngrass.quantity == 20

    def test_lawngrass_additional_attributes(self):
        """Дополнительные атрибуты."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        assert lawngrass.country == "Россия"
        assert lawngrass.germination_period == "7 дней"
        assert lawngrass.color == "Зеленый"


class TestLawngrassInheritance:

    def test_lawngrass_is_product(self):
        """Lawngrass наследует Product."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        assert isinstance(
            lawngrass,
            Product
        )

    def test_lawngrass_has_product_attributes(self):
        """Атрибуты Product доступны."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        assert hasattr(lawngrass, "name")
        assert hasattr(lawngrass, "description")
        assert hasattr(lawngrass, "price")
        assert hasattr(lawngrass, "quantity")

    def test_lawngrass_inherits_only_from_product(self):
        """Непосредственное наследование."""

        assert Lawngrass.__bases__ == (Product,)


class TestLawngrassStr:

    def test_lawngrass_str(self):
        """__str__."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        assert "Газонная трава" in str(lawngrass)
        assert "500.0 руб" in str(lawngrass)


class TestLawngrassAdd:

    def test_add_two_lawngrass(self):
        """Сложение двух газонных трав."""

        grass1 = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        grass2 = Lawngrass(
            "Трава 2",
            "Выносливая",
            450.0,
            15,
            "США",
            "5 дней",
            "Зеленый"
        )

        result = grass1 + grass2

        expected = (
            (500.0 * 20)
            + (450.0 * 15)
        )

        assert result == expected

    def test_add_lawngrass_and_product_raises(self):
        """Lawngrass + Product вызывает TypeError."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        with pytest.raises(TypeError):
            lawngrass + product


class TestLawngrassNewFunctionality:

    def test_lawngrass_repr(self):
        """Lawngrass использует __repr__ миксина."""

        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )

        assert repr(
            lawngrass
        ).startswith("Lawngrass(")

    def test_lawngrass_mixin_prints_creation_info(
        self,
        capsys
    ):
        """Миксин выводит информацию."""

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

        assert "Lawngrass" in captured.out
        assert "Газонная трава" in captured.out
        assert "Элитная трава" in captured.out
        assert "500.0" in captured.out
        assert "20" in captured.out