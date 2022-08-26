import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def print_text():
    print('\nСейчас будет много тестов)\n')
    yield None
    print('\nСпасибо за внимание!\n')


@pytest.fixture(scope='function')
def next_text():
    print('\nЭта нанало теста.\n')
    yield None
    print('\nА вот это конец.\n')
