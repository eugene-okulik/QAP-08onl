"""System module."""
# Задание 1
# Кликнуть все чекбоксы на странице.
# Их там 17. Открываются по клику на >
# https://demoqa.com/checkbox

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('window-size=640,960')
chrome_driver = webdriver.Chrome(options=options)


def click_checkbox(driver):
    """A dummy docstring."""
    driver.get('https://demoqa.com/checkbox')
    driver.execute_script("""
        var l = document.getElementById("fixedban").remove();
     """)

    for first_partition_toggle in driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn'):
        first_partition_toggle.click()
    for second_partition_toggle in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        second_partition_toggle.click()
    for third_partition_toggle in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        third_partition_toggle.click()
    for checkbox in driver.find_elements(By.CLASS_NAME, 'rct-checkbox'):
        checkbox.click()
        break

    sleep(3)
    driver.quit()


click_checkbox(chrome_driver)
