import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from .locators import Product


class ProductPage(BasePage):
    def buy_button_click(self):
        buy_button = WebDriverWait(self.browser, self.delay).until(
                EC.element_to_be_clickable(Product.Product.BUY_BUTTON))
        buy_button.click()
