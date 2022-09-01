"""System module."""
# Первый тест
# https://www.demoblaze.com/index.html
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


def test10_tabs(driver):
    """A dummy docstring."""
    driver.get("https://www.demoblaze.com/index.html")
    element = driver.find_element(By.CLASS_NAME, "h-100")
    element_text = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a").text
    ActionChains(driver).move_to_element(element).key_down(Keys.COMMAND)\
        .click(element).key_up(Keys.COMMAND).perform()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a").click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    cart = driver.find_element(By.XPATH, "//*[@id='cartur']")
    cart_text = driver.find_element(By.XPATH, "//*[@id='tbodyid']").text
    cart.click()
    time.sleep(5)
    assert cart_text in element_text
