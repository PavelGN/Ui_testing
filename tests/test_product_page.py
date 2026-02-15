from pages.product_page import ProductPage
from pages.shop_cart_page import ShopCartPage


def test_product_main_info_is_displayed(driver):
    product_page = ProductPage(driver)

    product_page.open_page()
    product_page.check_product_main_info_is_displayed()


def test_product_quantity_adds_correctly_to_cart(driver):
    product_page = ProductPage(driver)
    cart_page = ShopCartPage(driver)

    product_page.open_page()

    assert product_page.get_quantity_value() == "1"

    product_page.increase_quantity(2)
    product_page.add_to_cart()

    product_page.wait_cart_counter_is(3)

    product_page.go_to_cart()

    assert cart_page.get_product_quantity() == "3"


def test_product_can_be_removed_from_cart(driver):
    product_page = ProductPage(driver)
    cart_page = ShopCartPage(driver)

    product_page.open_page()

    product_page.add_product_to_cart()
    product_page.wait_cart_counter_is(1)
    product_page.go_to_cart()

    cart_page.remove_product()
    cart_page.check_cart_is_empty()
