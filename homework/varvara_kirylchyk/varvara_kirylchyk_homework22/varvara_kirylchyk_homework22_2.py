"""System module."""
# Второй тест
# https://demoqa.com/menu
# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 -
# здесь никакого ассерта не получится сделать

import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def test11(driver):
    """A dummy docstring."""
    driver.get("https://demoqa.com/menu")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element1 = driver.find_element(By.XPATH, "//*[@id=\"nav\"]/li[2]/a")
    element2 = driver.find_element(By.XPATH, "//*[@id=\"nav\"]/li[2]/ul/li[3]/a")
    element3 = driver.find_element(By.XPATH, "//*[@id=\"nav\"]/li[2]/ul/li[3]/ul/li[2]/a")
    ActionChains(driver).move_to_element(element1).pause(5).move_to_element(element2).\
        pause(5).move_to_element(element3).pause(5).click(element3).perform()
    time.sleep(5)
