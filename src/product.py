class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    products1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    products2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )
    products3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
    )

    print(products1.name)
    print(products1.description)
    print(products1.price)
    print(products1.quantity)

    print(products2.name)
    print(products2.description)
    print(products2.price)
    print(products2.quantity)

    print(products3.name)
    print(products3.description)
    print(products3.price)
    print(products3.quantity)
