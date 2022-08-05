from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)


def click_checkbox(driver):
    driver.get('https://demoqa.com/checkbox')

    for home_toggle_1st_level in driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn'):
        home_toggle_1st_level.click()
    for home_toggle_2nd_level in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        home_toggle_2nd_level.click()
    for home_toggle_3d_level in driver.find_elements(By.CLASS_NAME, 'rct-icon-expand-close'):
        home_toggle_3d_level.click()

    for checkbox_click in driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]'):
        checkbox_click.click()
        break


click_checkbox(driver)
