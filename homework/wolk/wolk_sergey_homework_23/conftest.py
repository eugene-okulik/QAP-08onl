import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def webdriver():
    Service(executable_path='chromedriver.exe')
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
