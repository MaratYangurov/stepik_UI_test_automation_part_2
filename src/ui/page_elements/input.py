from src.ui.page_elements.base import Base
import allure


class Input(Base):
    """Предовтавляет методы для работы с полями ввода"""

    def fill(self, text: str, delay: int|float = None):
        """Метод для ввода текста"""
        with allure.step(f'Введем текст "{text}" в поле ввода {self.allure_name}'):
            if delay:
                self._element.type(text=text, delay=delay)
            else:
                self._element.fill(value=text)

    def clear(self):
        """Очищает поле ввода"""
        with allure.step(f'Очистим поле ввода "{self.allure_name}"'):
            self._element.clear()
