# https://testpages.herokuapp.com/styled/alerts/alert-test.html
# Нажать на кнопку "Show prompt box", ввести в алерт какой-то ваш текст,
# нажать ок, проверить, что текст, который вы ввели появился под кнопкой.

"""module"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test3(chrome_driver):
    """module"""
    chrome_driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    chrome_driver.maximize_window()
    sleep(3)
    chrome_driver.find_element(By.ID, 'promptexample').click()
    sleep(3)
    Alert(chrome_driver).send_keys('changes')
    Alert(chrome_driver).accept()
    sleep(3)
    my_word = chrome_driver.find_element(By.ID, 'promptreturn')
    assert 'changes' in my_word.text
