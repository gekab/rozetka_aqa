import time

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
