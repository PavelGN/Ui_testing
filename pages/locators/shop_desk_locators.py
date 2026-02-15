from selenium.webdriver.common.by import By


class ShopDeskLocators:
    SORT_DROPDOWN = (
        By.XPATH,
        (
            "//div[contains(@class,'o_sortby_dropdown')]"
            "//a[@data-bs-toggle='dropdown']"
        ),
    )

    SORT_LOW_TO_HIGH = (
        By.XPATH,
        "//span[normalize-space()='Price - Low to High']"
    )

    PRODUCT_PRICES = (
        By.CSS_SELECTOR,
        ".oe_currency_value"
    )

    PRICE_SLIDER_READY = (
        By.CSS_SELECTOR,
        "input.ghost.multirange"
    )

    PRODUCTS = (
        By.CLASS_NAME,
        "oe_product_cart"
    )

    PRODUCT_PRICE = (
        By.CLASS_NAME,
        "oe_currency_value"
    )

    STEEL_FILTER = (
        By.XPATH,
        "//label[contains(text(),'Steel')]"
    )
