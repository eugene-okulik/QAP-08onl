# Третий тест
# https://testpages.herokuapp.com/styled/alerts/alert-test.html
# Нажать на кнопку "Show prompt box",
# ввести в алерт какой-то ваш текст, нажать ок,
# проверить, что текст, который вы ввели появился под кнопкой.

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test3(driver_chrome):
    driver_chrome.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver_chrome.maximize_window()
    sleep(3)
    driver_chrome.find_element(By.ID, 'promptexample').click()
    sleep(3)
    Alert(driver_chrome).send_keys('homework 22')
    Alert(driver_chrome).accept()
    sleep(3)
    check_word = driver_chrome.find_element(By.ID, 'promptreturn')
    assert 'homework 22' in check_word.text
