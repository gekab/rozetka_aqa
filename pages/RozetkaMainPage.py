import os
import time

# import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import BasePage
from pages.locators import Main


class MainPage(BasePage):
    def login_button_click(self):
        login_button = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.Header.LOGIN_BUTTON))
        login_button.click()

    def _switch_to_frame(self, iframes):
        self.browser.switch_to.frame(iframes)

    def login(self):
        email_input = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.LoginForm.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(self.LOGIN_ENV)

        password_input = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.LoginForm.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(self.PASSWD_ENV)

        enter_button = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.LoginForm.ENTER_BUTTON))
        enter_button.click()

        iframe = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.LoginForm.IFRAME))

        self._switch_to_frame(iframe)

        check_box_captcha = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.LoginForm.CHECK_BOX_CAPTCHA))
        check_box_captcha.click()

    def basket_button_click(self):
        WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.Header.BASKET_BUTTON)).click()

    def empty_basket_h4_text(self):
        basket_h4_text = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.Basket.EMPTY_BASKET_H4_TEXT))
        return basket_h4_text.text

    def change_language(self):
        WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.Header.CHANGE_LANG)).click()

    def catalog_button_click(self):
        catalog_button = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_element_located(Main.Main.Header.CATALOG_BUTTON))
        catalog_button.click()

    def check_brand_icons(self):
        menu_categories = WebDriverWait(self.browser, self.delay).until(
            EC.presence_of_all_elements_located(Main.Main.Header.FatMenu.MENU_CATEGORIES_SVG))

        for item in menu_categories:
            ActionChains(self.browser).move_to_element(item).pause(0.5).perform()
            main_brands = WebDriverWait(self.browser, self.delay).until(
                EC.presence_of_all_elements_located(Main.Main.Header.FatMenu.MAIN_BRANDS))
            for brand in main_brands:
                src_img_brand = brand.get_attribute("src")
                alt_img_brand = brand.get_attribute("alt")

                file_name = f"{src_img_brand.split('/')[-1]}"
                try:
                    brand.screenshot(f"./screenshots/ok_screen/{alt_img_brand}_{file_name}")
                except Exception as _ex:
                    print(_ex)
                    self.browser.save_screenshot(f"./screenshots/screenshot_error/{alt_img_brand}_{file_name}")

    def directory_must_be_empty(self, path_name):
        actual_result = len(os.listdir(path_name))
        expected_result = 0
        assert actual_result == expected_result, \
            f"The directory contains {actual_result} files with broken pictures of brands!"

    def click_on_element_from_sidebar_by_text(self, locator_text):
        time.sleep(1)
        selector = WebDriverWait(self.browser, self.delay).until(
            EC.element_to_be_clickable((By.XPATH,
                                                 f"//aside //*[contains(text(),'{locator_text}')and @class and @href]")))
        selector.click()
