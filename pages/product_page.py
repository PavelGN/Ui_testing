from pages.base_page import BasePage
from pages.locators.shop_product_page_locators import (
    ProductPageLocators as loc
)
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"


    def check_product_main_info_is_displayed(self):
        title = self.wait_for_visibility(loc.TITLE)
        assert title.text.strip() != ""

        price = self.wait_for_visibility(loc.PRICE)
        assert price.text.strip() != ""

        button = self.wait_for_clickable(loc.ADD_TO_CART_BUTTON)
        assert button.is_displayed()


    def check_default_quantity_is(self, expected_quantity):
        quantity = self.wait_for_visibility(loc.QUANTITY_INPUT)
        assert quantity.get_attribute("value") == str(expected_quantity)

    def increase_quantity(self, times=1):
        for _ in range(times):
            quantity_input = self.driver.find_element(*loc.QUANTITY_INPUT)
            old_value = int(quantity_input.get_attribute("value"))

            button = self.wait_for_clickable(loc.ADD_ONE_BUTTON)
            button.click()

            self.wait.until(
                lambda d: int(
                    d.find_element(*loc.QUANTITY_INPUT).get_attribute("value")
                ) > old_value
            )


    def add_to_cart(self):
        self.wait_for_clickable(loc.ADD_TO_CART_BUTTON).click()

    def wait_until_cart_counter_is(self, expected_value):
        self.wait.until(
            EC.text_to_be_present_in_element(
                loc.CART_COUNTER, str(expected_value)
            )
        )

    def check_cart_counter_is(self, expected_value):
        counter = self.wait_for_visibility(loc.CART_COUNTER)
        assert counter.text.strip() == str(expected_value)

    def go_to_cart(self):
        self.wait_for_clickable(loc.CART_LINK).click()

    def add_product_to_cart(self):
        self.add_to_cart()