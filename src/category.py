from src.product import Product
from src.exceptions import ZeroQuantityError


class CategoryProductsIterator:
    """Итератор по продуктам категории."""

    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        products = self._category._Category__products

        if self._index >= len(products):
            raise StopIteration

        product = products[self._index]
        self._index += 1

        return product


class Category:
    """Категория продуктов."""

    products_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products or []

        Category.products_count += len(self.__products)
        Category.category_count += 1

    def __str__(self):
        total_quantity = sum(
            product.quantity
            for product in self.__products
        )

        return (
            f"{self.name}, "
            f"количество продуктов: {total_quantity} шт."
        )

    def __iter__(self):
        return CategoryProductsIterator(self)

    def add_product(self, product):
        """Добавляет продукт в категорию."""

        try:
            if not isinstance(product, Product):
                raise TypeError(
                    "Можно добавлять только объект Product"
                )

            if product.quantity == 0:
                raise ZeroQuantityError(
                    "Товар с нулевым количеством "
                    "не может быть добавлен в категорию"
                )

        except (TypeError, ZeroQuantityError) as error:
            print(f"Ошибка: {error}")
            raise

        else:
            self.__products.append(product)
            Category.products_count += 1
            print("Товар успешно добавлен в категорию")

        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self):
        """Возвращает среднюю цену товаров категории."""

        try:
            total_price = sum(
                product.price
                for product in self.__products
            )

            return total_price / len(self.__products)

        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        if not self.__products:
            return ""

        return "\n".join(
            str(product)
            for product in self.__products
        )

    @classmethod
    @property
    def product_count(cls):
        return cls.products_count