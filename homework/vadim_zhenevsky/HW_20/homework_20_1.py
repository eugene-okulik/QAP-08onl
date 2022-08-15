from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(executable_path='chromedriver.exe')
Chrome_driver = webdriver.Chrome()
Chrome_driver.maximize_window()
Chrome_driver.get("https://demoqa.com/checkbox")

button_home = Chrome_driver.find_element(By.CLASS_NAME, "rct-collapse-btn")
button_home.click()

button_desktop = Chrome_driver.find_element(By.CLASS_NAME, "rct-icon-expand-close")
button_desktop.click()

button_documents = Chrome_driver.find_element(By.CLASS_NAME, "rct-icon-expand-close")
button_documents.click()

button_workspace = Chrome_driver.find_element(By.CLASS_NAME, "rct-icon-expand-close")
button_workspace.click()

button_office = Chrome_driver.find_element(By.CLASS_NAME, "rct-icon-expand-close")
button_office.click()

button_downloads = Chrome_driver.find_element(By.CLASS_NAME, "rct-icon-expand-close")
button_downloads.click()

desktop_checkbox = Chrome_driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
desktop_checkbox[1].click()

workspace_checkbox = Chrome_driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
workspace_checkbox[5].click()

public_checkbox = Chrome_driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
public_checkbox[10].click()

private_checkbox = Chrome_driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
private_checkbox[11].click()

classified_checkbox = Chrome_driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
classified_checkbox[12].click()

general_checkbox = Chrome_driver.find_elements(By.XPATH, '//span[@class="rct-title"]')
general_checkbox[13].click()

downloads_checkbox = Chrome_driver.find_elements(By.CLASS_NAME, "rct-checkbox")
downloads_checkbox[14].click()
