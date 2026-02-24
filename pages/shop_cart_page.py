from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.shop_cart_locators import ShopCartLocators as loc


class ShopCartPage(BasePage):
    page_url = '/shop/cart'


    def check_title_is(self, expected_text):
        element = self.wait_for_visibility(loc.TITLE)
        assert element.text.strip() == expected_text


    def check_cart_is_empty(self):
        element = self.wait_for_visibility(loc.EMPTY_CART_MESSAGE)
        assert element.text.strip() == "Your cart is empty!"


    def check_checkout_steps_are_visible(self):
        expected_steps = ["Review Order", "Shipping", "Payment"]

        for step in expected_steps:
            element = self.wait_for_visibility(
                (By.XPATH, f"//span[normalize-space()='{step}']")
            )
            assert element.is_displayed()


    def check_product_quantity_is(self, expected_quantity):
        quantity = self.wait_for_visibility((By.CLASS_NAME, "js_quantity"))
        assert quantity.get_attribute("value") == str(expected_quantity)


    def remove_product(self):
        product_row = self.wait_for_visibility(loc.PRODUCT_ROW)
        self.wait_for_clickable(loc.REMOVE_ONE_BUTTON).click()
        self.wait.until(EC.staleness_of(product_row))