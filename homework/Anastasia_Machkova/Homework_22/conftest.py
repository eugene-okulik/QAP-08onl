import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    #print('\nTest start\n')
    service = Service(executable_path='chromedriver.exe')
    driver_chrome = webdriver.Chrome(service=service)
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    #print('\nTest end\n')
    driver_chrome.quit()
