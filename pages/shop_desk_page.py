from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.shop_desk_locators import ShopDeskLocators as loc


class ShopDeskPage(BasePage):
    page_url = "/shop/category/desks-1"

    def check_products_are_sorted_by_price_low_to_high(self):
        sort_button = self.wait.until(
            EC.element_to_be_clickable(loc.SORT_DROPDOWN)
        )
        sort_button.click()

        self.wait.until(
            EC.element_to_be_clickable(loc.SORT_LOW_TO_HIGH)
        ).click()

        prices = self.wait.until(
            EC.visibility_of_all_elements_located(loc.PRODUCT_PRICES)
        )

        price_values = [
            float(price.text.replace("$", "").replace(",", "").strip())
            for price in prices
        ]

        assert price_values == sorted(price_values)

    def check_all_products_have_price(self):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(loc.PRODUCTS)
        )

        assert len(products) > 0

        for product in products:
            price = product.find_element(*loc.PRODUCT_PRICE)
            assert price.text.strip() != ""

    def check_steel_filter_changes_products(self):
        self.wait.until(
            EC.visibility_of_element_located(loc.PRICE_SLIDER_READY)
        )

        old_products = self.wait.until(
            EC.visibility_of_all_elements_located(loc.PRODUCTS)
        )
        old_count = len(old_products)

        steel_filter = self.wait.until(
            EC.element_to_be_clickable(loc.STEEL_FILTER)
        )
        steel_filter.click()

        self.wait.until(EC.url_contains("attrib=1-1"))

        new_products = self.wait.until(
            EC.visibility_of_all_elements_located(loc.PRODUCTS)
        )
        new_count = len(new_products)

        assert new_count != old_count
