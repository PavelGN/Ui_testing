import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.shop_cart_page import ShopCartPage
from pages.shop_desk_page import ShopDeskPage
from pages.product_page import ProductPage


@pytest.fixture()
def driver():
    options = Options()

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
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
