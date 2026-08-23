import pytest

from src.category import Category
from src.product import Product


class TestCategoryInit:
    """Тесты инициализации Category."""

    def test_category_init(self):
        """Создание категории."""
        category = Category(
            "Тест",
            "Описание"
        )

        assert category.name == "Тест"
        assert category.description == "Описание"

    def test_category_init_with_products(self):
        """Создание категории с продуктами."""
        products = [
            Product(
                "Тест",
                "Описание",
                100.0,
                10
            )
        ]

        category = Category(
            "Тест",
            "Описание",
            products
        )

        assert len(category._Category__products) == 1

    def test_category_str(self):
        """__str__ метод."""
        products = [
            Product(
                "Тест",
                "Описание",
                100.0,
                10
            )
        ]

        category = Category(
            "Тест",
            "Описание",
            products
        )

        assert "Тест" in str(category)
        assert "количество продуктов:" in str(category)


class TestCategoryAddProduct:
    """Тесты добавления продукта."""

    def test_add_product(self, empty_category):
        """Добавление продукта."""
        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        empty_category.add_product(product)

        assert product in empty_category._Category__products

    def test_add_product_increments_count(
        self,
        empty_category
    ):
        """Увеличение счётчика."""
        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        initial_count = Category.products_count

        empty_category.add_product(product)

        assert Category.products_count > initial_count

    def test_add_string_raises_typeerror(
        self,
        empty_category
    ):
        """Строка вызывает TypeError."""
        with pytest.raises(TypeError):
            empty_category.add_product("Not a product")

    def test_add_int_raises_typeerror(
        self,
        empty_category
    ):
        """Число вызывает TypeError."""
        with pytest.raises(TypeError):
            empty_category.add_product(123)

    def test_add_none_raises_typeerror(
        self,
        empty_category
    ):
        """None вызывает TypeError."""
        with pytest.raises(TypeError):
            empty_category.add_product(None)


class TestCategoryProducts:
    """Тесты property products."""

    def test_products_empty(self, empty_category):
        """Пустая категория."""
        assert empty_category.products == ""

    def test_products_with_items(self, smartphones_category):
        """Категория с продуктами."""
        products_str = smartphones_category.products

        assert "Samsung Galaxy S23 Ultra" in products_str


class TestCategoryIteration:
    """Тесты итерации."""

    def test_category_iteration(
        self,
        smartphones_category
    ):
        """Итерация по категории."""
        products = list(smartphones_category)

        assert len(products) == 3

    def test_category_iteration_values(
        self,
        smartphones_category
    ):
        """Значения при итерации."""
        products = list(smartphones_category)

        assert all(
            isinstance(product, Product)
            for product in products
        )


class TestCategoryProductCount:
    """Тесты product_count."""

    def test_product_count_class_attribute(self):
        """product_count как атрибут класса."""
        assert hasattr(Category, "products_count")

    def test_product_count_increases(
        self,
        empty_category
    ):
        """Увеличение product_count."""
        initial_count = Category.products_count

        empty_category.add_product(
            Product(
                "Тест",
                "Описание",
                100.0,
                10
            )
        )

        assert Category.products_count > initial_count