"""System module."""
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    """A dummy docstring."""
    chrome_driver = webdriver.Chrome()
    # driver.set_window_size(N, N)
    # driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    chrome_driver.quit()
