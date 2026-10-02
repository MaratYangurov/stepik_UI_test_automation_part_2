import allure

from src.ui.const import Data


@allure.story('Cтраница c товарами')
class TestProductPage:
    @allure.title('Проверка формирования хлебных крошек')
    def test_breadcrumb_cards(self, product_page):
        product_page.open()
        product_page.checkout_card_apple_shufle()
        product_page.check_breads_crumbs(Data.BREADCRUMB)