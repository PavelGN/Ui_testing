from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_ONE_BUTTON = (By.XPATH, "//a[@title='Add one']")
    ADD_TO_CART_BUTTON = (By.ID, "add_to_cart")
    QUANTITY_INPUT = (By.NAME, "add_qty")
    CART_COUNTER = (By.CLASS_NAME, "my_cart_quantity")
    CART_LINK = (By.CSS_SELECTOR, "a[href='/shop/cart']")
    TITLE = (By.XPATH, "//h1")
    PRICE = (By.CSS_SELECTOR, ".oe_price .oe_currency_value")
