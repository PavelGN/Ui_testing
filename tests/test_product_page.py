def test_product_main_info_is_displayed(product_page):
    product_page.open_page()

    assert product_page.get_title_text() != ""
    assert product_page.get_price_text() != ""
    assert product_page.is_add_to_cart_button_visible()


def test_product_quantity_adds_correctly_to_cart(product_page, cart_page):
    product_page.open_page()

    assert product_page.get_quantity_value() == "1"

    product_page.increase_quantity(2)
    product_page.add_to_cart()

    product_page.wait_until_cart_counter_is(3)

    assert product_page.get_cart_counter_value() == "3"

    product_page.go_to_cart()

    assert cart_page.get_product_quantity() == "3"


def test_product_can_be_removed_from_cart(product_page, cart_page):
    product_page.open_page()

    product_page.add_product_to_cart()
    assert product_page.get_cart_counter_value() == "1"

    product_page.go_to_cart()

    cart_page.remove_product()

    assert cart_page.get_empty_cart_message() == "Your cart is empty!"
