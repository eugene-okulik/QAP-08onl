import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    print('\nTest start\n')
    service = Service(executable_path='chromedriver.exe')
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    print('\nTest end\n')
    chrome_driver.quit()


@pytest.fixture(scope='session')
def all_tests():
    print('\nNow all tests will run\n')
    yield ""
    print('\nTesting is finished\n')
