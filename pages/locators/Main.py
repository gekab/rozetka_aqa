from selenium.webdriver.common.by import By


class Main:
    class MainManu:
        pass

    class Header:
        LOGIN_BUTTON = (By.CSS_SELECTOR, "rz-user button.header__button")
        BASKET_BUTTON = (By.CSS_SELECTOR, "rz-cart button.header__button")
        CHANGE_LANG = (By.CSS_SELECTOR, "a.lang__link")
        CATALOG_BUTTON = (By.ID, "fat-menu")

        class FatMenu:
            MENU_CATEGORIES = (By.CSS_SELECTOR, "div.menu-wrapper.menu-wrapper_state_animated li.menu-categories__item")
            MENU_CATEGORIES_SVG = (By.CSS_SELECTOR, "div.menu-wrapper.menu-wrapper_state_animated "
                                                    "li.menu-categories__item svg.menu-categories__link-chevron")
            MAIN_BRANDS_A = (By.CSS_SELECTOR, "li.menu__main-brand a")
            MAIN_BRANDS = (By.CSS_SELECTOR, "li.menu__main-brand img")

    class Sidebar:
        pass

    class LoginForm:
        EMAIL_INPUT = (By.ID, "auth_email")
        PASSWORD_INPUT = (By.ID, "auth_pass")
        REMEMBER_ME_CHECK_BOX = (By.ID, "remember_me")
        ENTER_BUTTON = (By.CSS_SELECTOR, "button.auth-modal__submit")
        CHECK_BOX_CAPTCHA = (By.CSS_SELECTOR, "span.rc-anchor-checkbox")
        IFRAME = (By.CSS_SELECTOR, "rz-re-captcha div > iframe")
