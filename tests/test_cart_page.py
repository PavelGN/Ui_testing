from pages.shop_cart_page import ShopCartPage


def test_cart_page_title(driver):
    page = ShopCartPage(driver)
    page.open_page()

    page.check_title_is("Order overview")


def test_empty_cart_message(driver):
    page = ShopCartPage(driver)
    page.open_page()

    page.check_empty_cart_message_is("Your cart is empty!")


def test_checkout_steps(driver):
    page = ShopCartPage(driver)
    page.open_page()

    page.check_checkout_steps_are_visible()
