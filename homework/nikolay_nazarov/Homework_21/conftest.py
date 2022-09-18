import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def print_text_multiple_times():
    print('\nevery_func_fixture - before')
    yield None
    print('\nevery_func_fixture - after')


@pytest.fixture(scope='session')
def print_text_once():
    print('\nevery_session_fixture - before session')
    yield None
    print('every_session_fixture - after session')
