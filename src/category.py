from src.product import Product

class Category:
    name: str
    description: str
    products: list
    products_count = 0
    category_count = 0



    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products or []
        Category.products_count += len(self.products)
        Category.category_count += 1



if __name__ == "__main__":
    products1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    products2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    products3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [products1, products2, products3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.products_count)

    products4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [products4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.products_count)