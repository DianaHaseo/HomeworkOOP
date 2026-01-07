from src.product import Product
from src.category import Category


def main():
    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Категория 1: Смартфоны
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("=== Категория Смартфоны ===")
    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1.products)  # ✅ Геттер возвращает строку
    print(f"Категорий: {Category.category_count}, Продуктов: {Category.products_count}")
    print()

    # Добавление продукта через add_product()
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)  # ✅ Или создайте category2 ниже
    print("После add_product():")
    print(category1.products)
    print(f"Продуктов: {Category.products_count}")  # ✅ +1 к счетчику
    print()

    # Категория 2: Телевизоры (для проверки category_count)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром",
        []
    )
    print("=== Категория Телевизоры ===")
    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(f"Всего категорий: {Category.category_count}")  # ✅ 2
    print(f"Всего продуктов: {Category.products_count}")
    print()

    # Тест new_product()
    new_product = Product.new_product({
        "name": "New Samsung",
        "description": "Test desc",
        "price": 180000.0,
        "quantity": 3
    })
    print("=== new_product() ===")
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
    print()

    # Тест сеттера цены
    print("=== Тест сеттера цены ===")
    new_product.price = 800  # ✅ Положительная цена
    print(new_product.price)

    new_product.price = -100  # ❌ Отрицательная → сообщение
    print(new_product.price)  # Не изменилась

    new_product.price = 0  # ❌ Нулевая → сообщение
    print(new_product.price)  # Не изменилась


if __name__ == "__main__":
    main()
