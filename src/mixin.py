class ProductMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args, **kwargs):
        print(
            f"Создан объект класса {self.__class__.__name__} "
            f"с параметрами: {args}"
        )

        super().__init__(*args, **kwargs)

    def __repr__(self):
        params = []

        for value in self.__dict__.values():
            params.append(repr(value))

        return (
            f"{self.__class__.__name__}"
            f"({', '.join(params)})"
        )