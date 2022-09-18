import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    print('\nSTART\n')
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    print('\nEND\n')
    driver.quit()
