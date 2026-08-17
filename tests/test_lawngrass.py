import pytest
from src.product import Product
from src.lawngrass import Lawngrass


class TestLawngrassInit:
    """Тесты инициализации Lawngrass"""

    def test_lawngrass_init(self):
        """Создание газонной травы"""
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
        """Дополнительные атрибуты"""
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
    """Тесты наследования"""

    def test_lawngrass_is_product(self):
        """Lawngrass наследует Product"""
        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )
        assert isinstance(lawngrass, Product)

    def test_lawngrass_has_product_attributes(self):
        """Атрибуты Product доступны"""
        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )
        assert hasattr(lawngrass, 'name')
        assert hasattr(lawngrass, 'description')
        assert hasattr(lawngrass, 'price')
        assert hasattr(lawngrass, 'quantity')


class TestLawngrassStr:
    """Тесты __str__"""

    def test_lawngrass_str(self):
        """__str__ метод"""
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
    """Тесты сложения"""

    def test_add_two_lawngrass(self):
        """Сложение двух газонных трав"""
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
        expected = (500.0 * 20) + (450.0 * 15)
        assert result == expected

    def test_add_lawngrass_and_product_raises(self):
        """Сложение травы и Product вызывает TypeError"""
        lawngrass = Lawngrass(
            "Газонная трава",
            "Элитная трава",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый"
        )
        product = Product("Тест", "Описание", 100.0, 10)
        with pytest.raises(TypeError):
            lawngrass + product