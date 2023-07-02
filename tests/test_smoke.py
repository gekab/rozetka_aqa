import time

import pytest
from selenium.common import StaleElementReferenceException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

from pages import MainPage


# @pytest.mark.skip
class TestMain:
    @pytest.mark.skip
    def test_guest_can_open_site(self, browser):
        main_page = MainPage(browser, "https://rozetka.com.ua")
        main_page.open()
        # time.sleep(15)

    @pytest.mark.skip
    def test_guest_can_open_login_form(self, browser_chrome):
        main_page = MainPage(browser_chrome, "https://rozetka.com.ua")
        main_page.open()
        main_page.login_button_click()
        main_page.login()
        time.sleep(60)

    def test_empty_basket(self, browser):
        # expected_result = "Кошик порожній"
        expected_result = ["Кошик порожній", "Корзина пуста"]
        main_page = MainPage(browser, "https://rozetka.com.ua/ua")
        main_page.open()
        main_page.change_language()
        try:
            main_page.basket_button_click()
        except StaleElementReferenceException as _ex:
            print(_ex)
            main_page.basket_button_click()
        assert main_page.empty_basket_h4_text() in expected_result
