from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from pages.locators import Basket


class BasketPage(BasePage):
    def _basket_locator_h3(self):
        return WebDriverWait(self.browser, self.delay).until(
                EC.presence_of_element_located(Basket.Basket.Header.H3_TEXT))

    def return_basket_h3_text(self):
        return self._basket_locator_h3().text

    def order_table_is(self):
        try:
            return WebDriverWait(self.browser, self.delay).until(
                EC.presence_of_all_elements_located(Basket.Basket.Content.CART_LIST_ITEMS))
        except Exception as e:
            print(f"Помилка :{e}")
            return []

    def get_product_name(self, product):
        return WebDriverWait(product, self.delay).until(EC.visibility_of_element_located(Basket.Basket.Content.
                                                                                      CART_ITEM_TITLE)).text

    def print_all_cart_items(self):
        index = 0
        print("\n=====Список назв товарів у корзині=====")
        for item in self.order_table_is():
            index += 1
            print(index, ": ", self.get_product_name(item))

    def click_on_triple_dot_product(self, product):
        triple_dot = WebDriverWait(product, self.delay).until(
            EC.element_to_be_clickable(Basket.Basket.Content.TRIPLE_DOT_PRODUCT))
        triple_dot.click()

    def click_on_triple_dot_delete_button(self, product):
        triple_dot_delete_button = WebDriverWait(product, self.delay).until(
            EC.element_to_be_clickable(Basket.Basket.Content.TRIPLE_DOT_DELETE_BUTTON))
        triple_dot_delete_button.click()

    def get_the_text_that_the_basket_is_empty(self):
        try:
            return WebDriverWait(self.browser, self.delay).until(
                EC.element_to_be_clickable(Basket.Basket.Content.EMPTY_BASKET_H4_TEXT)).text
        except Exception as e:
            print(f"Помилка! Кошик не порожній!!! ")
            return "1111"
