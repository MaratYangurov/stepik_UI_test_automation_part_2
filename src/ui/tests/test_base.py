import allure

from src.ui.const import Data


@allure.story('Главная страница')
class TestBasePage:
    @allure.title('Проверка перехода в карточку товара')
    def test_check_cards(self, base_page):
        base_page.open()
        base_page.check_desktop_apple(Data.APPLE)


    allure.title('Проверка оплаты товара')
    def test_by_decices(self, base_page, cart_page):
        base_page.open()
        base_page.checkout_htc_and_ad_to_card(Data.HTC)
        cart_page.check_number_devices()
        cart_page.checkout_product()