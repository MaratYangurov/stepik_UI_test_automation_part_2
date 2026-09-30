from pathlib import Path

import pytest

from src.ui.browser.browser_launcher import BrowserLauncher
from src.ui.pages.base_page import BasePage
from src.ui.pages.cart_page import CartPage


config_yaml_path = Path(__file__).parent.parent / 'config_browser.yaml'


@pytest.fixture(scope='function')
def browser():
    brw = BrowserLauncher(config_yaml_path)
    new_page = brw.create_page()

    yield new_page

    brw.close()

# @pytest.fixture(scope='function')
# def browser():
#     playwright = sync_playwright().start()
#     browser = playwright.chromium.launch(channel='chrome',headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     browser.close()
#     playwright.stop()

@pytest.fixture(scope='function')
def base_page(browser):
    return BasePage(browser)

@pytest.fixture(scope='function')
def cart_page(browser):
    return CartPage(browser)