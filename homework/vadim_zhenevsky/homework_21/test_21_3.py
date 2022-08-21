import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


serv = Service(executable_path='chromedriver.exe')
chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(10)


@pytest.fixture(scope='session')
def start_now():
    print("START")
    yield chrome_driver
    print("END")
    chrome_driver.quit()


def test_click_buttons_1(start_now):
    chrome_driver.get('https://testpages.herokuapp.com/styled/'
                      'dynamic-buttons-simple.html')
    start_button = chrome_driver.find_element(By.ID, 'button00')
    start_button.click()
    one_button = chrome_driver.find_element(By.ID, 'button01')
    one_button.click()
    two_button = chrome_driver.find_element(By.ID, 'button02')
    two_button.click()
    tree_button = chrome_driver.find_element(By.ID, 'button03')
    tree_button.click()
    text_check = chrome_driver.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in text_check.text
    print(text_check.text)


def test_click_buttons_2(start_now):
    chrome_driver.get('https://testpages.herokuapp.com/'
                      'styled/dynamic-buttons-disabled.html')
    start_button = chrome_driver.find_element(By.ID, 'button00')
    start_button.click()
    one_button = chrome_driver.find_element(By.ID, 'button01')
    two_button = chrome_driver.find_element(By.ID, 'button02')
    three_button = chrome_driver.find_element(By.ID, 'button03')
    WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable(one_button))
    one_button.click()
    WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable(two_button))
    two_button.click()
    WebDriverWait(chrome_driver, 10).until(ec.element_to_be_clickable(three_button))
    three_button.click()
    text_check = chrome_driver.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in text_check.text
    print(text_check.text)
