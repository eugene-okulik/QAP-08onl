from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path='chromedriver.exe')

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

driver.get('https://demoqa.com/checkbox')
open_all_checkbox = driver.find_element(By.CLASS_NAME, 'rct-option')
open_all_checkbox.click()

sleep(3)

driver.quit()
