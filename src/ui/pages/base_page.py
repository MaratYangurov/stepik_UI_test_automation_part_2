import allure
from playwright.sync_api import Page, expect

from src.ui.browser.browser import Browser
from src.ui.helper.urls import BASE_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.element import Element
from src.ui.page_elements.input import Input
from src.ui.page_elements.text import Text


class BasePage:
    """Логика для тестов на главной странице."""

    def __init__(self, page: Page, url=BASE_URL):
        self.page = page
        self.url = url
        self.browser = Browser(page)
        self.button_all_categoty = Button(page, stratagy='by_role', role='button', value='All Categories', allure_name='All Categories')
        self.button_desktop = Button(page, stratagy='locator', selector="//a[text()='Desktops'])[1]", allure_name='Desktop')
        self.input_search = Input(page, stratagy='locator', selector="//input[@name='search'])[1]", allure_name='Поле ввода')
        self.button_search = Button(page, stratagy='by_role', role='button', value='Search',
                                          allure_name='Search')
        self.element_card = Element(page, stratagy='locator', selector='locator', allure_name='Карточки с товаром')
        self.element_breadcrumb = Element(page, stratagy='locator', selector='.breadcrumb-item', allure_name='Хлебные крошки')

    def open(self):
        """Открываем страницу по url"""
        return self.browser.go_to_url(self.url)

    def check_breads_crumbs(self, breads_crumbs: list):
        """Проверяет формирование хлебных крошек
        :param breads_crumbs: хлебные крошки, в нужном порядке (напр. [Главная, Вторая, Третья])
        :type breads_crumbs: list"""
        with allure.step('Проверяем формирование хлебных крошек'):
            for idx in range(1, self.element_breadcrumb.count()+1):
                loc = self.element_breadcrumb.get_element().nth(idx)
                expect(loc).to_have_text(breads_crumbs[idx])

    def check_desktop_apple(self, search_name, cards=15):
        """Проверяет переход в карточки товара"""
        with allure.step('Выберем Desktop из списка'):
            self.button_all_categoty.click()
            self.button_desktop.click()
        with allure.step('Введем название поля ввода'):
            self.input_search.fill(search_name)

        self.input_search.click()

        with allure.step('Проверим, что карточки с товаром доступны'):
            self.element_card.get_element().first.wait_for(state='visible')
            coutner_card = self.element_card.get_element().count()
            assert coutner_card == cards