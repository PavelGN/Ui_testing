from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators.shop_desk_locators import ShopDeskLocators as loc


class ShopDeskPage(BasePage):
    page_url = "/shop/category/desks-1"


    def apply_sorting_by_price_low_to_high(self):
        self.wait_for_clickable(loc.SORT_DROPDOWN).click()
        self.wait_for_clickable(loc.SORT_LOW_TO_HIGH).click()

    def check_products_are_sorted_by_price_low_to_high(self):
        prices = self.wait_for_all_visible(loc.PRODUCT_PRICES)

        price_values = [
            float(price.text.replace("$", "").replace(",", "").strip())
            for price in prices
        ]

        assert price_values == sorted(price_values)


    def check_all_products_have_price(self):
        products = self.wait_for_all_visible(loc.PRODUCTS)

        assert len(products) > 0

        for product in products:
            price = product.find_element(*loc.PRODUCT_PRICE)
            assert price.text.strip() != ""


    def apply_steel_filter(self):
        self.wait_for_visibility(loc.PRICE_SLIDER_READY)
        self.wait_for_clickable(loc.STEEL_FILTER).click()
        self.wait.until(EC.url_contains("attrib=1-1"))

    def get_products_count(self):
        products = self.wait_for_all_visible(loc.PRODUCTS)
        return len(products)

    def check_products_count_changed(self, old_count):
        new_products = self.wait_for_all_visible(loc.PRODUCTS)
        new_count = len(new_products)

        assert new_count != old_count