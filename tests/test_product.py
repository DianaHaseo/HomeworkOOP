import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_categories_from_json(path: str):
    data = read_json(path)
    categories = []
    for cat_data in data:
        products = [Product(**p) for p in cat_data['products']]
        categories.append(Category(cat_data['name'],
                                 cat_data['description'],
                                 products))
    return categories


if __name__ == "__main__":
    # Скачайте products.json и положите в ../data/
    categories = create_categories_from_json("../data/products.json")
    print(f"Загружено категорий: {len(categories)}")
    for cat in categories:
        print(f"Категория: {cat.name}, товаров: {len(cat.products)}")