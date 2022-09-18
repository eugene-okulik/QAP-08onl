# Написать автотесты для сайта http://automationpractice.com/
# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов)) должны быть такими,
# чтобы Pytest понял, что это тесты)

# Задание 3
# Проверить, что сообщение “Invalid email address.”
# появляется если ввести слово “мыло” в поле емейл и попытаться создать аккаунт

"""Module providingFunction printing python version."""
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome_driver.get("http://automationpractice.com")

service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)


@pytest.fixture(scope='function')
def test_email_driver():
    """module"""
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield
    chrome_driver.quit()

def test_email_address():
    """module"""
    chrome_driver.get('http://automationpractice.com/')
    sing_in = chrome_driver.find_element(By.XPATH, '//a[@class="login"]')
    sing_in.click()
    email_address = chrome_driver.find_element(By.ID, 'email_create')
    email_address.send_keys('мыло')
    button = chrome_driver.find_element(By.ID, 'SubmitCreate')
    button.click()
    chrome_driver.implicitly_wait(10)
    alert_danger = chrome_driver.find_element(By.CLASS_NAME, 'alert-danger')
    alert_danger_text = alert_danger.find_element(By.TAG_NAME, 'li')
    assert "Invalid email address." in alert_danger_text.text
    chrome_driver.quit()
