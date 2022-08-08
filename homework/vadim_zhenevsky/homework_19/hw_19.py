from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://automationpractice.com/')

contact_us_button = driver.find_element(By.ID, 'contact-link')
contact_us_button.click()

Subject_Heading = Select(driver.find_element(By.ID, "id_contact"))
Subject_Heading.select_by_value("1")

email_field = driver.find_element(By.ID, "email")
email_field.send_keys('vadim@mail.com')

reference_field = driver.find_element(By.ID, "id_order")
reference_field.send_keys('I did it!)')

Attach_File = driver.find_element(By.XPATH, "//input[@type='file']")
Attach_File.send_keys('C:/Users/v.zhenevskiy/Desktop/УЧЕБА/2022.txt')

massage = driver.find_element(By.ID, "message")
massage.send_keys('Hello everyone!')

submit_button = driver.find_element(By.NAME, 'submitMessage')
submit_button.click()

Successful_message = driver.find_element(By.ID, 'center_column')
Successful_message = Successful_message.find_element(By.TAG_NAME, "P")
print(Successful_message.text)

sleep(3)

driver.quit()
