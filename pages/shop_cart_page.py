from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.shop_cart_locators import ShopCartLocators as loc


class ShopCartPage(BasePage):
    page_url = '/shop/cart'

    def get_title_text(self):
        element = self.wait_for_visibility(loc.TITLE)
        return element.text.strip()

    def get_empty_cart_message(self):
        element = self.wait_for_visibility(loc.EMPTY_CART_MESSAGE)
        return element.text.strip()

    def get_checkout_steps(self):
        steps = ["Review Order", "Shipping", "Payment"]
        visible_steps = []

        for step in steps:
            element = self.wait_for_visibility(
                (By.XPATH, f"//span[normalize-space()='{step}']")
            )
            if element.is_displayed():
                visible_steps.append(step)

        return visible_steps

    def get_product_quantity(self):
        quantity = self.wait_for_visibility((By.CLASS_NAME, "js_quantity"))
        return quantity.get_attribute("value")

    def remove_product(self):
        product_row = self.wait_for_visibility(loc.PRODUCT_ROW)
        self.wait_for_clickable(loc.REMOVE_ONE_BUTTON).click()
        self.wait.until(EC.staleness_of(product_row))
