import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def set_up():
    print("Вы вошли в систему")
    yield
    print("Вы вышли из системы")


@pytest.fixture(scope='function')
def action():
    print("Начало")
    yield
    print("Конец")


@pytest.fixture(scope='function')
def driver():
    opt = Options()
    opt.add_argument('--start-maximized')
    serv = Service(executable_path='D:\\driver\\chromedriver.exe')
    driver1 = webdriver.Chrome(service=serv, options=opt)
    driver1.implicitly_wait(10)
    yield driver1
    driver1.quit()


@pytest.fixture(scope='function')
def driver2():
    opt = Options()
    opt.add_argument('window-size=760,1080')
    serv = Service(executable_path='D:\\driver\\chromedriver.exe')
    driver_ch = webdriver.Chrome(service=serv, options=opt)
    driver_ch.implicitly_wait(10)
    yield driver_ch
    driver_ch.quit()
