from src.product import Product
from src.category import Category


def main():
    print("=== Демонстрация заданий ===\n")

    # Создание продуктов
    prod1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    prod2 = Product("iPhone 15", "512GB, Gray space", 210000.0, 8)
    prod3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # ✅ Задание 1+2: приватный список + геттер
    category1 = Category("Смартфоны", "Описание смартфонов", [prod1, prod2, prod3])
    print("✅ Категория 1 (геттер products):")
    print(category1.products)
    print(f"Категорий: {Category.category_count}, Продуктов: {Category.products_count}\n")

    # ✅ Задание 1: add_product
    prod4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(prod4)
    print("✅ После add_product():")
    print(category1.products)
    print(f"Продуктов: {Category.products_count}\n")

    # ✅ Задание 3: new_product из словаря
    new_prod_data = {
        "name": "New Samsung",
        "description": "Test desc",
        "price": 90000.0,
        "quantity": 2
    }
    new_prod = Product.new_product(new_prod_data)
    print("✅ new_product из словаря:")
    print(f"{new_prod.name}: {new_prod.price} руб., {new_prod.quantity} шт.\n")

    # ✅ Задание 4: тесты setter
    print("✅ Тесты цены:")
    print(f"Начальная цена: {new_prod.price}")

    new_prod.price = 100000.0  # ✅ Повышение - OK
    print(f"После повышения: {new_prod.price}")

    new_prod.price = 0  # ❌ <= 0 - сообщение
    print(f"После 0: {new_prod.price} (не изменилась)")

    new_prod.price = -100  # ❌ Отрицательная
    print(f"После -100: {new_prod.price} (не изменилась)\n")

    # ✅ Дополнительное Задание 3: дубликат
    products_list = [prod1]
    dup_data = {"name": "Samsung Galaxy S23 Ultra", "description": "дубликат",
                "price": 200000.0, "quantity": 3}
    updated_prod = Product.new_product(dup_data, products_list)
    print("✅ Дубликат (доп. задание 3):")
    print(f"Обновленный: {updated_prod.name}, цена: {updated_prod.price}, кол-во: {updated_prod.quantity}")

    # ✅ Дополнительное Задание 4: понижение цены
    print("\n✅ Понижение цены (доп. задание 4):")
    print("Введите 'y' для подтверждения или 'n' для отмены:")


if __name__ == "__main__":
    main()
