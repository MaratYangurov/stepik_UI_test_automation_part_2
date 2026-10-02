from playwright.sync_api import Page

from src.ui.helper.urls import APPLE_DEVICES_URL, BASE_URL
from src.ui.page_elements.text import Text
from src.ui.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page, url=BASE_URL+APPLE_DEVICES_URL):
        super().__init__(page, url)
        self.ipad_shuffle = Text(page, stratagy='locator', selector="//*[text()='iPod Shuffle']",
                                 allure_name="iPod Shuffle")

    def checkout_card_apple_shufle(self):
        """Переходит в карточку товара iPad Shuffle"""
        self.ipad_shuffle.click()
