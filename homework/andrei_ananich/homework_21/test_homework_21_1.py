# Написать автотесты для сайта http://automationpractice.com/
# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов)) должны быть такими,
# чтобы Pytest понял, что это тесты)

# Задание 1
# Проверить, что в самом низу главной страницы есть текст
# “© 2014 Ecommerce software by PrestaShop™”
""" module """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)
chrome_driver.implicitly_wait(10)
chrome_driver.maximize_window()
chrome_driver.get("http://automationpractice.com/")


def test():
    """module"""
    assert chrome_driver.find_element(By.CSS_SELECTOR,
                               "#footer > div > section.bottom-footer.col-xs-12 > div").text == \
           "© 2014 Ecommerce software by PrestaShop™"
    chrome_driver.quit()
