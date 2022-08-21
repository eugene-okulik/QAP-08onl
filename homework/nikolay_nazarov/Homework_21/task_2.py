from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope='function')
def driver():
    print('\nbefore test\n')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    print('\nafter test\n')
    driver.quit()


class TestTask:

    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    @pytest.mark.skip
    @pytest.mark.usefixtures('driver')
    def test_blank_text(self):
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        blank_text = self.driver.find_element(By.CLASS_NAME, "_blank").text
        assert blank_text == "Ecommerce software by PrestaShop™", "В самом низу главной страницы нет текста " \
                                                                  "Ecommerce software by PrestaShop™"

    @pytest.mark.usefixtures('driver')
    def test_logo_is_visible(self):
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        print("1")
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице"
        print("2")
        self.driver.find_element(By.CSS_SELECTOR, "[title = 'Women']").click()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице"
        print("3")
        self.driver.find_element(By.CSS_SELECTOR, "[title = 'Dresses']").click()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице"
        print("4")
        self.driver.find_element(By.CSS_SELECTOR, "[title = 'T-shirts']").click()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице"


