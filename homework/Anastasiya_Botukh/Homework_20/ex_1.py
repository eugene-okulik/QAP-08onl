from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('window-size=2048,1080')
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/checkbox")
open_all = driver.find_element(By.CLASS_NAME, "rct-icon-expand-all")
open_all.click()
select = driver.find_element(By.CLASS_NAME, "rct-checkbox")
select.click()

sleep(3)

close_all = driver.find_element(By.CLASS_NAME, "rct-icon-expand-open")
close_all.click()

sleep(2)

driver.quit()
