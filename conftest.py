import pytest
from selenium import webdriver

from pages.shop_cart_page import ShopCartPage
from pages.shop_desk_page import ShopDeskPage
from pages.product_page import ProductPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def cart_page(driver):
    return ShopCartPage(driver)


@pytest.fixture
def desk_page(driver):
    return ShopDeskPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)
