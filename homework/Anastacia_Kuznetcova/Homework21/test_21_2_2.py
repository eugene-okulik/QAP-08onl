from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest


serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
driver = webdriver.Chrome(service=serv)


@pytest.fixture(scope='session')
def start_now():
    print("Начинаем")
    driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html")
    yield driver
    print("Заканчиваем")
    driver.quit()


# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument, no-self-use
def test_7(start_now):
    driver.find_element(By.ID, "button00").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button01").is_displayed()
    driver.implicitly_wait(5)


def test_8():
    driver.find_element(By.ID, "button01").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button02").is_displayed()
    driver.implicitly_wait(5)


def test_9():
    driver.find_element(By.ID, "button02").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, "button03").is_displayed()
    driver.implicitly_wait(5)


def test_10():
    driver.find_element(By.ID, "button03").click()
    assert driver.find_element(By.ID, "buttonmessage").text == \
           'All Buttons Clicked'
