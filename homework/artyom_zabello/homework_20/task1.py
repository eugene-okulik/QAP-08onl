from time import sleep
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv = Service(executable_path="C:\\Scripts\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=serv)


def click_checkboxes(driver):
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    button_for_checkboxes = driver.find_element(By.CLASS_NAME, 'rct-icon-expand-all')
    button_for_checkboxes.click()
    checkboxes = driver.find_elements(By.CLASS_NAME, 'rct-icon-uncheck')
    try:
        for i in checkboxes:
            i.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        sleep(1)
        driver.quit()


click_checkboxes(chrome_driver)
