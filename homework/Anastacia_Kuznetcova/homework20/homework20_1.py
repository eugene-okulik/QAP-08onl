from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
Chrome_driver = webdriver.Chrome(service=serv)
Chrome_driver.maximize_window()


def click_checkboxes(chrome_driver):
    chrome_driver.get('https://demoqa.com/checkbox')

    for toggle_part_1 in chrome_driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn'):
        toggle_part_1.click()
    for toggle_part_2 in chrome_driver.find_elements(By.CLASS_NAME,
                                                     'rct-icon-expand-close'):
        toggle_part_2.click()
    for toggle_part_3 in chrome_driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        toggle_part_3.click()

    for checkbox_click in chrome_driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]'):
        checkbox_click.click()
        break


click_checkboxes(Chrome_driver)
