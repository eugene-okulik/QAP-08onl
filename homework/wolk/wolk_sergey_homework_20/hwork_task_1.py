import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

service = Service(executable_path='chromedriver.exe')
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def click_checkboxes(driver):
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    but_box = driver.find_element(By.CLASS_NAME, 'rct-icon-expand-all')
    but_box.click()
    checkbox = driver.find_elements(By.CLASS_NAME, 'rct-icon-uncheck')
    try:
        for i in checkbox:
            i.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        sleep(1)
        driver.quit()


click_checkboxes(driver)
