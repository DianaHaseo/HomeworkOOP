def _get_product():
    from src.product import Product
    return Product


class Lawngrass(_get_product()):
    """Газонная трава - наследник Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color