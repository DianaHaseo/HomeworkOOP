class ZeroQuantityError(ValueError):
    """Исключение при добавлении товара с нулевым количеством."""

    def __init__(
        self,
        message="Товар с нулевым количеством не может быть добавлен"
    ):
        super().__init__(message)