import time

import pytest
from selenium.common import StaleElementReferenceException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

from pages import MainPage
from pages import CategoryPage
from pages import CatalogPage
# from pages.locators import Main


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

    # @pytest.mark.skip
    def test_empty_basket(self, browser):
        # expected_result = "Кошик порожній"
        expected_result = ["Кошик порожній", "Корзина пуста"]
        main_page = MainPage(browser, "https://rozetka.com.ua/ua")
        # main_page.open()
        main_page.change_language()
        try:
            main_page.basket_button_click()
        except StaleElementReferenceException as _ex:
            print(_ex)
            main_page.basket_button_click()
        assert main_page.empty_basket_h4_text() in expected_result

    # @pytest.mark.skip
    def test_brand_icons_in_categories(self, browser):
        main_page = MainPage(browser, "https://rozetka.com.ua/ua")
        main_page.catalog_button_click()
        main_page.check_brand_icons()
        main_page.directory_must_be_empty("./screenshots/screenshot_error")

    def test_guest_can_add_product_to_basket(self, browser):
        main_page = MainPage(browser, "https://rozetka.com.ua/ua")
        main_page.click_on_element_from_sidebar_by_text("Зоотовар")
        current_page_link = browser.current_url
        category_page = CategoryPage(browser, current_page_link)
        category_page.click_on_element_from_category_by_text("Собак")
        category_page.click_on_element_from_category_by_text("Корм")
        current_page_link = browser.current_url
        catalog_page = CatalogPage(browser, current_page_link)
        catalog_page.click_on_product_for_index(3)
        time.sleep(3)
