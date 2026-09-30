import allure

from src.ui.const import Data


@allure.story('Главная страница')
class TestBasePage:
    @allure.title('Проверка перехода в карточку товара')
    def test_check_cards(self, base_page):
        base_page.open()
        base_page.check_desktop_apple(Data.APPLE)

