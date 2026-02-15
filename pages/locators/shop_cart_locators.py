from selenium.webdriver.common.by import By


class ShopCartLocators:
    TITLE = (By.XPATH, "//h3")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".js_cart_lines.alert-info")
    PRODUCT_ROW = (By.CSS_SELECTOR, "div.o_cart_product")
    REMOVE_ONE_BUTTON = (By.XPATH, "//a[@title='Remove one']")
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, "js_cart_lines")
