import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver_chrome():
    serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
    driver = webdriver.Chrome(service=serv)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def print_text():

    print('\nTesting loading\n')
    yield None
    print('\nEnd!\n')


@pytest.fixture(scope='function')
def text_inside_test():
    print('\nНачало проверки теста\n')
    yield None
    print('\nКонец проверки теста\n')
