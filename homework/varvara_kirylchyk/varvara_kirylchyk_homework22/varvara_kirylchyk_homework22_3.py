"""System module."""
# Третий тест
# https://testpages.herokuapp.com/styled/alerts/alert-test.html
# Нажать на кнопку "Show prompt box",
# ввести в алерт какой-то ваш текст, нажать ок,
# проверить, что текст, который вы ввели появился под кнопкой.


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test11(driver):
    """A dummy docstring."""
    driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
    driver.find_element(By.ID, 'promptexample').click()
    time.sleep(3)
    Alert(driver).send_keys('test')
    time.sleep(3)
    Alert(driver).accept()
    check_text = driver.find_element(By.ID, 'promptreturn')
    assert check_text.text == 'test'
    time.sleep(3)
