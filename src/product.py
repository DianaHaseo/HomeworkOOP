class Product:
    """Базовый класс продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов - только одинаковые типы"""
        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, data: dict, products_list=None):
        """Создание продукта из словаря с проверкой дубликатов"""
        name = data["name"]
        if products_list:
            for existing in products_list:
                if existing.name == name:
                    new_price = max(existing.price, data["price"])
                    existing.quantity += data["quantity"]
                    existing.price = new_price
                    return existing
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Установка цены с подтверждением при понижении"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirm = input("Цена понижается. Подтвердить? (y/n): ").lower()
            if confirm != 'y':
                print("Изменение цены отменено")
                return
        self.__price = new_price