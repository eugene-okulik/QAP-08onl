import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    opt = Options()
    opt.add_argument('--start-maximized')
    serv = Service(executable_path='D:\\driver\\chromedriver.exe')
    driver_chrome = webdriver.Chrome(options=opt, service=serv)
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
