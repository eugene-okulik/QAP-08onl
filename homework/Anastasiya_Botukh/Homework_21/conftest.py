import pytest

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope='function')
def every_session():
    print("\nSTART")
    yield
    print("\nEND")


@pytest.fixture(scope='session')
def some_sessions():
    print("\nBEFORE")
    yield
    print("\nAFTER")


@pytest.fixture(scope='function')
def driver():
    print('\nSTART\n')
    options = Options()
    options.add_argument('window-size=2048,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    print('\nTHE END\n')
    driver.quit()
