from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path='C:/Users/Марго/Desktop/TMS/chromedriver.exe')
    driver_chrome = webdriver.Chrome(service=service)
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
