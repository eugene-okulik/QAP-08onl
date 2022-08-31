import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
