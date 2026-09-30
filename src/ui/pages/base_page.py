from playwright.sync_api import Page

from src.ui.browser.browser import Browser
from src.ui.helper.urls import BASE_URL, CART_URL
from src.ui.page_elements.element import Element
from src.ui.page_elements.text import Text


class BasePage:
    """Логика для тестов на главной странице."""

    def __init__(self, page: Page, url=BASE_URL):
        self.page = page
        self.url = url
        self.browser = Browser(page)
        self.text_monitors = Text(page, stratagy='by_text', value='Monitors', allure_name='Monitors')
        self.text_apple_monitors = Text(page, stratagy='by_text', value='Apple monitor 24', allure_name='Apple monitor 24')
        self.elemment_card = Element(page, stratagy='locator', selector='.card-block', allure_name='Карточка товара')
        self.text_card = Text(page, stratagy='locator', selector='#cartur', allure_name='Корзина')

    def open(self):
        """Открываем страницу по url"""
        return self.browser.go_to_url(self.url)

    def switching_to_monitors(self):
        """Кликает на мониторы"""
        self.text_monitors.click()
        self.text_apple_monitors.wait_for(state='visible')

    def check_cards(self, number_of_cards: int):
        """Проверяет кол-во карточек с товаром
        :param number_of_cards: количество карточек с товаром"""
        cnt = self.elemment_card.get_element().count()
        assert cnt == number_of_cards

    def switching_to_card(self):
        """Кликает на мониторы"""
        self.text_card.click()
        assert CART_URL in self.page.url
