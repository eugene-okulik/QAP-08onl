# Кликнуть все чекбоксы на странице.
# Их там 17. Открываются по клику на >
# https://demoqa.com/checkbox

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path='../Homework_21/chromedriver.exe')
chrome_driver = webdriver.Chrome(service=service)


def click_checkbox(driver):
    driver.get('https://demoqa.com/checkbox')
    driver.maximize_window()

    for first_partition_toggle in driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn'):
        first_partition_toggle.click()
    for second_partition_toggle in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        second_partition_toggle.click()
    for third_partition_toggle in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        third_partition_toggle.click()
    for checkbox in driver.find_elements(By.CLASS_NAME, 'rct-checkbox'):
        checkbox.click()
        break

    sleep(15)
    driver.quit()


click_checkbox(chrome_driver)
