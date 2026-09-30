import allure


class TestCartPage:
    @allure.title('Проверка кнопки "Place order"')
    def test_card(self, cart_page):
        cart_page.open()
        cart_page.check_place_order_button()
