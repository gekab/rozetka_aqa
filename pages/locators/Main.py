from selenium.webdriver.common.by import By


class Main:
    class MainMane:
        pass

    class Header:
        LOGIN_BUTTON = (By.CSS_SELECTOR, "rz-user button.header__button.ng-star-inserted")
        BASKET_BUTTON = (By.CSS_SELECTOR, "ul.header-actions button.header__button")
        CHANGE_LANG = (By.CSS_SELECTOR, "a.lang__link")

    class Basket:
        EMPTY_BASKET_H4_TEXT = (By.CSS_SELECTOR, "h4.cart-dummy__heading")

    class Sidebar:
        pass

    class LoginForm:
        EMAIL_INPUT = (By.ID, "auth_email")
        PASSWORD_INPUT = (By.ID, "auth_pass")
        REMEMBER_ME_CHECK_BOX = (By.ID, "remember_me")
        ENTER_BUTTON = (By.CSS_SELECTOR, "button.auth-modal__submit")
        CHECK_BOX_CAPTCHA = (By.CSS_SELECTOR, "span.rc-anchor-checkbox")
        IFRAME = (By.CSS_SELECTOR, "rz-re-captcha div > iframe")
