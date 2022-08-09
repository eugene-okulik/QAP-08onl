from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
Chrome_driver = webdriver.Chrome(service=serv)
Chrome_driver.get("https://demoqa.com/checkbox")
all_checkboxes = Chrome_driver.find_element(By.CLASS_NAME, "rct-checkbox")
all_checkboxes.click()
expend_all = Chrome_driver.find_element(By.CSS_SELECTOR, '#tree-node > div >\n'
                                                         ' button.rct-option.rct-option-expand-all')
expend_all.click()
