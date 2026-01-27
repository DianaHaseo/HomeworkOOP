from src.product import Product

class Category:
    name: str
    description: str
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products or []  # ✅ Задание 1: приватный
        Category.products_count += len(self.__products)
        Category.category_count += 1

    def add_product(self, product: Product):  # ✅ Задание 1
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products(self):  # ✅ Задание 2: геттер
        if not self.__products:
            return ""
        result = []
        for p in self.__products:
            result.append(f"{p.name}, {int(p.price)} руб. Остаток: {p.quantity} шт.")
        return "\n".join(result)
