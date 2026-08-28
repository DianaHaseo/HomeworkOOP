import pytest

from src.exceptions import ZeroQuantityError


class TestZeroQuantityError:
    """Тесты пользовательского исключения."""

    def test_zero_quantity_error_is_value_error(self):
        """Проверка наследования от ValueError."""
        assert issubclass(ZeroQuantityError, ValueError)

    def test_zero_quantity_error_message(self):
        """Проверка сообщения исключения."""
        with pytest.raises(
            ZeroQuantityError,
            match="Товар с нулевым количеством не может быть добавлен"
        ):
            raise ZeroQuantityError()

    def test_zero_quantity_error_custom_message(self):
        """Проверка собственного сообщения."""
        with pytest.raises(
            ZeroQuantityError,
            match="Тестовое сообщение"
        ):
            raise ZeroQuantityError("Тестовое сообщение")