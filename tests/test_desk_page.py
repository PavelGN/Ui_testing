def test_products_sorted_by_price(desk_page):
    desk_page.open_page()

    desk_page.apply_sorting_by_price_low_to_high()
    prices = desk_page.get_prices()

    assert prices == sorted(prices)


def test_all_products_have_price(desk_page):
    desk_page.open_page()

    assert desk_page.get_products_count() > 0
    assert desk_page.all_products_have_price()


def test_steel_filter_changes_products(desk_page):
    desk_page.open_page()

    old_count = desk_page.get_products_count()

    desk_page.apply_steel_filter()

    new_count = desk_page.get_products_count()

    assert new_count != old_count
