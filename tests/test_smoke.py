import datetime
import time

import pytest
from selenium.common import StaleElementReferenceException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages import MainPage
from pages import CategoryPage
from pages import CatalogPage
from pages import ProductPage
from pages import BasketPage
from pages.locators import Main


# @pytest.mark.skip
class TestMain:

    @staticmethod
    def save_screenshot_for_test(self, test_name):
        time_str = str(datetime.datetime.now()).replace(":", "_").split(".")[0]
        time_str = time_str.replace(" ", "_")
        self.browser.save_screenshot(f"./screenshots/{test_name.__name__}_" + f"{time_str}.png")

    @staticmethod
    def add_product_in_cart(browser, product_index):
        main_page = MainPage(browser, "https://rozetka.com.ua/ua")
        main_page.click_on_element_from_sidebar_by_text("Смарт")
        current_page_link = browser.current_url
        category_page = CategoryPage(browser, current_page_link)
        category_page.click_on_element_from_category_by_text("Телев")
        # category_page.click_on_element_from_category_by_text("Корм")
        current_page_link = browser.current_url
        catalog_page = CatalogPage(browser, current_page_link)
        catalog_page.click_on_product_for_index(product_index)
        product_page = ProductPage(browser, browser.current_url)
        product_page.buy_button_click()

    @staticmethod
    def delete_from_cart_all_products(browser):
        current_page_link = browser.current_url
        basket_page = BasketPage(browser, current_page_link)
        if len(basket_page.order_table_is()) > 0:
            print("З кошика будуть видалені такі продукті:")
            print(basket_page.print_all_cart_items())

            for product in basket_page.order_table_is():
                basket_page.click_on_triple_dot_product(product)
                basket_page.click_on_triple_dot_delete_button(product)
        else:
            print("Кошик порожній")

    # @pytest.mark.skip
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
            assert main_page.empty_basket_h4_text() in expected_result, "Кошик не порожній!"
        except StaleElementReferenceException as _ex:
            print(f"Виникла помилка: {_ex}")
            main_page.basket_button_click()

    # @pytest.mark.skip
    def test_brand_icons_in_categories(self, browser):
        main_page = MainPage(browser, "https://rozetka.com.ua/ua")
        main_page.catalog_button_click()
        main_page.check_brand_icons()
        main_page.directory_must_be_empty("./screenshots/screenshot_error")

    # @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser):
        try:
            self.add_product_in_cart(browser, 4)
            browser.get("https://rozetka.com.ua/ua")
            self.add_product_in_cart(browser, 5)
            browser.get("https://rozetka.com.ua/ua")
            self.add_product_in_cart(browser, 8)

            # main_page = MainPage(browser, "https://rozetka.com.ua/ua")
            # main_page.basket_button_click()

            basket_url = browser.current_url
            basket_page = BasketPage(browser, basket_url)

            # Відкрито кошик - модальне вікно з текстом "Кошик" для Н3
            assert basket_page.return_basket_h3_text() in ["Кошик", "Корзина"], \
                "Модальне вікно КОШИКА не відкрито"

            # На сторінці Кошика є таблиця товарів - список елементів таблиці товарів "cart-list__item"
            assert basket_page.order_table_is(), "Кошик порожній, і не містить товарів"
        except Exception as e:
            print(f"Помилка!\n{e}")
            # self.save_screenshot_for_test(self.test_guest_can_add_product_to_basket)
            time_str = str(datetime.datetime.now()).replace(":", "_").split(".")[0]
            time_str = time_str.replace(" ", "_")
            browser.save_screenshot(f"./screenshots/{self.test_guest_can_add_product_to_basket.__name__}_" + f"{time_str}.png")

        self.delete_from_cart_all_products(browser)

    # @pytest.mark.skip
    def test_guest_can_delete_products_from_basket(self, browser):
        self.add_product_in_cart(browser, 4)
        self.delete_from_cart_all_products(browser)

        basket_url = browser.current_url
        basket_page = BasketPage(browser, basket_url)
        assert basket_page.get_the_text_that_the_basket_is_empty() in ["Кошик порожній", "Корзина пуста"], "кошик не порожній і містить товарі"

    # @pytest.mark.skip
    def test_check_shopping_cart_not_empty(self, browser):
        self.add_product_in_cart(browser, 9)
        # try:
        basket_url = browser.current_url
        basket_page = BasketPage(browser, basket_url)

        assert basket_page.order_table_is(), "Кошик порожній, і не містить товарів"

        basket_page.print_all_cart_items()

        # except Exception as _ex:
        #     print(f"Виникла помилка: {_ex}")
        #     time_str = str(datetime.datetime.now()).replace(":", "_").split(".")[0]
        #     time_str = time_str.replace(" ", "_")
        #     browser.save_screenshot(f"./screenshots/{self.test_check_shopping_cart_not_empty.__name__}_" + f"{time_str}.png")

        self.delete_from_cart_all_products(browser)
