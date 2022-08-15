from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

def check_alert(driver):
    driver.get(' http://automationpractice.com/')
    contact_us_button = driver.find_element(By.ID, 'contact-link')
    contact_us_button.click()
    submit_button = driver.find_element(By.NAME, 'submitMessage')
    submit_button.click()
    alert_block = driver.find_element(By.CLASS_NAME, 'alert-danger')
    assert 'Invalid email address' in alert_block.text
#print(alert_block.text)

#url = driver.current_url
#title = driver.title

driver.quit()
#print(url, title)

def check_alert_header(driver):
    driver.get(' http://automationpractice.com/')
    contact_us_button = driver.find(By.PARTIAL_LINK_TEXT, "Contact")
    contact_us_button.click()
    email_field = driver.find_element()