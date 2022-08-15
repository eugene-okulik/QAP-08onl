from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

service = Service(executable_path='chromedriver.exe')

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

driver.get('http://automationpractice.com/')
contact_button = driver.find_element(By.ID, 'contact-link')
contact_button.click()

subject_heading = Select(driver.find_element(By.ID, 'id_contact'))
subject_heading.select_by_value('2')

email_address = driver.find_element(By.ID, 'email')
email_address.click()
email_address.send_keys('nastya.machkova98@gmail.com')

order_reference = driver.find_element(By.ID, 'id_order')
order_reference.click()
order_reference.send_keys('12345')

upload_file = driver.find_element(By.ID, "fileUpload")
attach_file = driver.find_element(By.XPATH, "//input[@type='file']")
attach_file.send_keys('C:/Users/a.machkova.MACHKOVA-T490/Desktop/myfile.txt')

sleep(3)

message = driver.find_element(By.ID, 'message')
message.send_keys('I have a problem!')

sleep(2)

send_button = driver.find_element(By.NAME, 'submitMessage')
send_button.click()

Successfully_send = driver.find_element(By.ID, 'center_column').find_element(By.TAG_NAME, 'P')
print(Successfully_send.text)

sleep(3)

driver.quit()
