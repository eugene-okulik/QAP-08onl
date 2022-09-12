from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import settings


@pytest.fixture(scope='function')
def driver(browser_option):
    options = Options()
    # options.add_argument('window-size=1920,1080')
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    # if browser_option == 'ff':
    if settings.BROWSER_NAME == 'ff':
        with allure.step('Run Firefox'):
            my_driver = webdriver.Firefox()
    elif settings.BROWSER_NAME == 'chrome':
        with allure.step('Run Chrome'):
            my_driver = webdriver.Chrome(options=options)
    my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action='store',
        default='chrome',
        help='Укажите название браузера, по умолчанию значение - chrome'
    )


@pytest.fixture(scope='session')
def browser_option(request):
    return request.config.getoption('--browser')
