import allure
from playwright.sync_api import Page

from src.ui.const import InputData
from src.ui.helper.urls import BASE_URL, PAYMENT_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.element import Element
from src.ui.page_elements.input import Input
from src.ui.page_elements.text import Text
from src.ui.pages.base_page import BasePage


class PaymentPage(BasePage):
    def __init__(self, page: Page, url=BASE_URL+PAYMENT_URL):
        super().__init__(page, url)
        self.field_first_name = Input(page, stratagy='locator', selector='#input-payment-firstname',
                                      allure_name='First name')
        self.field_last_name = Input(page, stratagy='locator', selector='#input-payment-lastname',
                                      allure_name='Last name')
        self.field_email = Input(page, stratagy='locator', selector='#input-payment-email',
                                    allure_name='Email')
        self.field_telephone = Input(page, stratagy='locator', selector='#input-payment-telephone',
                                allure_name='Telephone')
        self.field_password = Input(page, stratagy='locator', selector='#input-payment-password',
                                     allure_name='Password')
        self.field_password_confirm = Input(page, stratagy='locator', selector='#input-payment-confirm',
                                    allure_name='Password Confirm')
        self.field_address_1 = Input(page, stratagy='locator', selector='#input-payment-address_1',
                                    allure_name='Address 1')
        self.field_city = Input(page, stratagy='locator', selector='#input-payment-city',
                                     allure_name='City')
        self.field_post_code = Input(page, stratagy='locator', selector='#input-payment-postcode ',
                                allure_name='Post code')
        self.checkbox_privacy_policy = Text(page, stratagy='locator', selector="//*[text()='I have read and agree to the '])[1]",
                                            allure_name='Чекбокс 1')
        self.checkbox_terms_and_conditions = Text(page, stratagy='locator',
                                            selector="//*[text()='I have read and agree to the '])[2]",
                                            allure_name='Чекбокс 2')
        self.button_continue = Button(page, stratagy='by_role', role='button', value='Continue ', allure_name='Continue')

    def input_field_and_continue(self):
        with allure.step('Заполним формы'):
            self.field_first_name.fill(InputData.FIRST_NAME, delay=50)
            self.field_last_name.fill(InputData.LAST_NAME, delay=50)
            self.field_email.fill(InputData.EMAIL, delay=50)
            self.field_telephone.fill(InputData.TELEPHONE, delay=50)
            self.field_password.fill(InputData.PASSWORD, delay=50)
            self.field_password_confirm.fill(InputData.PASSWORD, delay=50)
            self.field_address_1.fill(InputData.ADDRESS_1, delay=50)
            self.field_city.fill(InputData.CITY, delay=50)
            self.field_post_code.fill(InputData.POST_CODE, delay=50)
        with allure.step('Проставим чек-боксы'):
            self.checkbox_privacy_policy.click()
            self.checkbox_terms_and_conditions.click()
        self.button_continue.click()
