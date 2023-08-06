from selenium.webdriver.common.by import By


class Basket:
    class Header:
        H3_TEXT = (By.CSS_SELECTOR, "h3.modal__heading")

    class Content:
        EMPTY_BASKET_H4_TEXT = (By.CSS_SELECTOR, "h4.cart-dummy__heading")
        CART_LIST_ITEMS = (By.CSS_SELECTOR, "ul.cart-list li.cart-list__item")
        CART_ITEM_TITLE = (By.CSS_SELECTOR, "a.cart-product__title")
        TRIPLE_DOT_PRODUCT = (By.CSS_SELECTOR, "button.button--white")
        TRIPLE_DOT_DELETE_BUTTON = (By.CSS_SELECTOR, "button.button--medium.button--with-icon.button--link")
