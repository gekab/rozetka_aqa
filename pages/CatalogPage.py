import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from pages.locators import Catalog


class CatalogPage(BasePage):
    def click_on_product_for_index(self, index: int):
        product = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        f"section.content li.catalog-grid__cell:nth-of-type({index%self.delimiter})")))
        product.click()
