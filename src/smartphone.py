def _get_product():
    from src.product import Product
    return Product


class Smartphone(_get_product()):
    """Смартфон - наследник Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color