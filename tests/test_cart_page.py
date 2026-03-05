import pytest


@pytest.mark.smoke
def test_cart_page_title(cart_page):
    cart_page.open_page()
    cart_page.check_title_is("Order overview")


@pytest.mark.smoke
def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.check_cart_is_empty()


@pytest.mark.smoke
def test_checkout_steps(cart_page):
    cart_page.open_page()
    cart_page.check_checkout_steps_are_visible()
