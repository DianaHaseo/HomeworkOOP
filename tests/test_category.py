import pytest

from src.category import Category
from src.product import Product


class TestCategoryInit:

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
            empty_category.add_product(
                "Not a product"
            )

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

    def test_products_empty(self, empty_category):
        """Пустая категория."""

        assert empty_category.products == ""

    def test_products_with_items(
        self,
        smartphones_category
    ):
        """Категория с продуктами."""

        products_str = smartphones_category.products

        assert "Samsung Galaxy S23 Ultra" in products_str


class TestCategoryIteration:

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

    def test_product_count_class_attribute(self):
        """product_count как атрибут класса."""

        assert hasattr(
            Category,
            "products_count"
        )

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


class TestCategoryMiddlePrice:
    """Тесты новой функциональности."""

    def test_middle_price(self):
        """Средняя цена товаров."""

        products = [
            Product(
                "Товар 1",
                "Описание",
                100.0,
                10
            ),
            Product(
                "Товар 2",
                "Описание",
                200.0,
                5
            ),
            Product(
                "Товар 3",
                "Описание",
                300.0,
                2
            )
        ]

        category = Category(
            "Категория",
            "Описание",
            products
        )

        assert category.middle_price() == 200.0

    def test_middle_price_does_not_use_quantity(
        self
    ):
        """Средняя цена считается без учёта количества."""

        products = [
            Product(
                "Товар 1",
                "Описание",
                100.0,
                100
            ),
            Product(
                "Товар 2",
                "Описание",
                200.0,
                1
            )
        ]

        category = Category(
            "Категория",
            "Описание",
            products
        )

        assert category.middle_price() == 150.0

    def test_middle_price_empty_category(
        self,
        empty_category
    ):
        """Для пустой категории возвращается 0."""

        assert empty_category.middle_price() == 0

from src.exceptions import ZeroQuantityError


class TestCategoryZeroQuantity:

    def test_zero_quantity_product_raises_error(
        self,
        empty_category
    ):
        """Товар с нулевым количеством нельзя добавить."""

        product = Product.__new__(Product)

        product.name = "Товар"
        product.description = "Описание"
        product.quantity = 0

        with pytest.raises(ZeroQuantityError):
            empty_category.add_product(product)

    def test_successful_add_prints_messages(
        self,
        empty_category,
        capsys
    ):
        """Успешное добавление выводит сообщения."""

        product = Product(
            "Товар",
            "Описание",
            100.0,
            5
        )

        empty_category.add_product(product)

        captured = capsys.readouterr()

        assert "Товар успешно добавлен в категорию" in captured.out
        assert "Обработка добавления товара завершена" in captured.out

    def test_zero_quantity_prints_finally_message(
        self,
        empty_category,
        capsys
    ):
        """finally выполняется даже при ошибке."""

        product = Product.__new__(Product)

        product.name = "Товар"
        product.description = "Описание"
        product.quantity = 0

        with pytest.raises(ZeroQuantityError):
            empty_category.add_product(product)

        captured = capsys.readouterr()

        assert (
            "Обработка добавления товара завершена"
            in captured.out
        )