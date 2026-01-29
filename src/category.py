from src.product import Product


class CategoryProductsIterator:
    """✅ Итератор по продуктам категории"""
    def __init__(self, category):
        self._category = category  # Сохраняем объект категории
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._category._Category__products):  # Правильный name mangling
            raise StopIteration
        product = self._category._Category__products[self._index]
        self._index += 1
        return product


class Category:
    name: str
    description: str
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products or []
        Category.products_count += len(self.__products)
        Category.category_count += 1

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryProductsIterator(self)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products(self):
        if not self.__products:
            return ""
        return "\n".join(str(p) for p in self.__products)