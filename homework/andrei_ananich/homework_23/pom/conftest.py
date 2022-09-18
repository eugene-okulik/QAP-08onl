"""modules"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver():
    """modules"""
    options = Options()
    options.add_argument('window-size=1920,1080')
    service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                      "andrei_ananich\\selenium\\chromedriver.exe")
    chrome_driver = webdriver.Chrome(service=service)
    # chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()
