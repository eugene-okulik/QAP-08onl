# Кликнуть все чекбоксы на странице. Их там 17.
# Открываются по клику на >
# https://demoqa.com/checkbox

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)
chrome_driver.maximize_window()


def click_checkbox(driver):
    driver.get('https://demoqa.com/checkbox')
    driver.maximize_window()

    for toggle_home in driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn'):
        toggle_home.click()
    for toggle_home_1st_line in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        toggle_home_1st_line.click()
    for toggle_home_2d_line in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        toggle_home_2d_line.click()
    for toggle_home_3d_line in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        toggle_home_3d_line.click()

    for checkbox_click in driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]'):
        checkbox_click.click()
        break


click_checkbox(chrome_driver)
