def test_cart_page_title(cart_page):
    cart_page.open_page()

    assert cart_page.get_title_text() == "Order overview"


def test_empty_cart_message(cart_page):
    cart_page.open_page()

    assert cart_page.get_empty_cart_message() == "Your cart is empty!"


def test_checkout_steps(cart_page):
    cart_page.open_page()

    steps = cart_page.get_checkout_steps()

    assert steps == ["Review Order", "Shipping", "Payment"]
