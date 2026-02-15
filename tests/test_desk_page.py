from pages.shop_desk_page import ShopDeskPage


def test_products_sorted_by_price(driver):
    page = ShopDeskPage(driver)
    page.open_page()

    page.check_products_are_sorted_by_price_low_to_high()


def test_all_products_have_price(driver):
    page = ShopDeskPage(driver)
    page.open_page()

    page.check_all_products_have_price()


def test_steel_filter_changes_products(driver):
    page = ShopDeskPage(driver)
    page.open_page()

    page.check_steel_filter_changes_products()
