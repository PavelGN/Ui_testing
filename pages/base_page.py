from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def open_page(self):
        if self.page_url:
            full_url = f"{self.base_url}{self.page_url}"
            self.driver.get(full_url)
        else:
            raise NotImplementedError(
                "Page cannot be opened for this page class"
            )

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait_for_visibility(self, locator: tuple):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_all_visible(self, locator: tuple):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    def wait_for_clickable(self, locator: tuple):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
