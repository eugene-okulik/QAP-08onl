from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.quit()
