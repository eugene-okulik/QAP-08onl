import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
    driver_chrome = webdriver.Chrome(service=serv)
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
