import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from pages.locators import Category


class CategoryPage(BasePage):
    def click_on_element_from_category_by_text(self, locator_text):
        selector = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//rz-widget-list //*[contains(text(),'{locator_text}')"
                                        f"and @class and @href]")))
        selector.click()
