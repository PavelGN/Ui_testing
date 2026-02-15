from pages.base_page import BasePage
from pages.locators.shop_product_page_locators import (
    ProductPageLocators as loc
)


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"

    def get_quantity_value(self):
        quantity = self.wait_for_visibility(loc.QUANTITY_INPUT)
        return quantity.get_attribute("value")

    def increase_quantity(self, times=1):
        for _ in range(times):
            button = self.wait_for_clickable(loc.ADD_ONE_BUTTON)
            button.click()

    def add_to_cart(self):
        self.wait_for_clickable(loc.ADD_TO_CART_BUTTON).click()

    def wait_cart_counter_is(self, expected_value):
        self.wait.until(
            lambda d: d.find_element(
                *loc.CART_COUNTER
            ).text == str(expected_value)
        )

    def go_to_cart(self):
        self.wait_for_clickable(loc.CART_LINK).click()

    def check_product_main_info_is_displayed(self):
        title = self.wait_for_visibility(loc.TITLE)
        assert title.text.strip() != ""

        price = self.wait_for_visibility(loc.PRICE)
        assert price.text.strip() != ""

        add_button = self.wait_for_clickable(loc.ADD_TO_CART_BUTTON)
        assert add_button.is_displayed()

    def add_product_to_cart(self):
        self.wait_for_clickable(loc.ADD_TO_CART_BUTTON).click()
