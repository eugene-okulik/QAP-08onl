import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
driver = webdriver.Chrome(service=serv)


@pytest.fixture(scope='session')
def start_now():
    print("Начинаем")
    driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
    time.sleep(3)
    yield driver
    print("Заканчиваем")
    driver.quit()


# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument, no-self-use
def test11(start_now):
    driver.find_element(By.ID, 'button00').click()
    time.sleep(5)
    btn_1 = driver.find_element(By.ID, 'button01')
    btn_2 = driver.find_element(By.ID, 'button02')
    btn_3 = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn_1))
    btn_1.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn_2))
    btn_2.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn_3))
    btn_3.click()
    assert driver.find_element(By.ID, "buttonmessage").text == \
           'All Buttons Clicked'
    time.sleep(5)
    driver.quit()
