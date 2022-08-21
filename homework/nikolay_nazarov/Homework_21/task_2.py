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


def test_blank_text(driver):
    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    blank_text = driver.find_element(By.CLASS_NAME, "_blank").text
    assert blank_text == "Ecommerce software by PrestaShop™", "В самом низу главной страницы нет текста " \
                                                              "Ecommerce software by PrestaShop™"

def test_screen_is_visible(driver):
    driver.get("http://automationpractice.com/")
    driver.maximize_window()
    blank_text = driver.find_element(By.CSS_SELECTOR, "[alt="My Store"]").src
    assert blank_text == "Ecommerce software by PrestaShop™", "В самом низу главной страницы нет текста " \
                                                              "Ecommerce software by PrestaShop™"
