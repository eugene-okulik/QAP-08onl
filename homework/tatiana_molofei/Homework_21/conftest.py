import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver_chrome = webdriver.Chrome(options=options)
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
