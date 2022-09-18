# Тесты должны запускаться с помощью Pytest
# (т.е. их названия (тестов, файла(ов)) должны быть такими,
# чтобы Pytest понял, что это тесты)

# Задание 2
# Проверить, что логотип отображается во всех трех категориях сайта (woman, dresses, t-shirts)

""" module """
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)
chrome_driver.implicitly_wait(10)
chrome_driver.maximize_window()
chrome_driver.get("http://automationpractice.com/")


@pytest.fixture(scope='function')
def test_tabs_driver():
    """module"""
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    chrome_driver.get("http://automationpractice.com/")
    yield chrome_driver
    chrome_driver.quit()


def test_women():
    """A dummy docstring."""
    chrome_driver.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[1]/a").click()
    chrome_driver.implicitly_wait(5)
    assert chrome_driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test_dresses():
    """A dummy docstring."""
    chrome_driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()
    assert chrome_driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test_t_shirts():
    """A dummy docstring."""
    chrome_driver.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[3]/a").click()
    assert chrome_driver.find_element(By.CLASS_NAME, "logo").is_displayed()
    chrome_driver.quit()
