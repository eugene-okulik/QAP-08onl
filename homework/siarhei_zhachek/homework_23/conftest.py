import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    # driver.set_window_size(600, 1110)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    # driver.set_window_size(660, 880)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
