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

    def wait_until_cart_counter_is(self, expected_value):
        self.wait.until(
            lambda driver: driver.find_element(
                *loc.CART_COUNTER
            ).text == str(expected_value)
        )

    def add_to_cart(self):
        self.wait_for_clickable(loc.ADD_TO_CART_BUTTON).click()

    def get_cart_counter_value(self):
        counter = self.wait_for_visibility(loc.CART_COUNTER)
        return counter.text.strip()

    def go_to_cart(self):
        self.wait_for_clickable(loc.CART_LINK).click()

    def get_title_text(self):
        title = self.wait_for_visibility(loc.TITLE)
        return title.text.strip()

    def get_price_text(self):
        price = self.wait_for_visibility(loc.PRICE)
        return price.text.strip()

    def is_add_to_cart_button_visible(self):
        button = self.wait_for_clickable(loc.ADD_TO_CART_BUTTON)
        return button.is_displayed()

    def add_product_to_cart(self):
        self.add_to_cart()
