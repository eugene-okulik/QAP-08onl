# Напишите программу, которая зайдет на сайт
# http://automationpractice.com/, кликнет по ссылке Contact us,
# полностью заполнит форму и нажмет Send.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)
chrome_driver.maximize_window()
chrome_driver.get("https://automationpractice.com/")

contact_us = chrome_driver.find_element(By.ID, 'contact-link')
contact_us.click()

subject_heading = chrome_driver.find_element(By.ID, 'id_contact')
subject_heading.click()
select = Select(chrome_driver.find_element(By.ID, 'id_contact'))
select.select_by_value("2")

email_address_field = chrome_driver.find_element(By.ID, 'email')
email_address_field.send_keys("andrei.ananich@gmail.com")

order_reference_field = chrome_driver.find_element(By.ID, 'id_order')
order_reference_field.send_keys("test1")

message_field = chrome_driver.find_element(By.ID, 'message')
message_field.send_keys("Check my order")

attached_file_field = chrome_driver.find_element(By.XPATH, "//input[@type='file']")
attached_file_field.send_keys("C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                              "andrei_ananich\\selenium\\test.txt")
sleep(2)
send_button = chrome_driver.find_element(By.ID, 'submitMessage')
send_button.click()

text = chrome_driver.find_element(By.ID, 'center_column')
text1 = text.find_element(By.TAG_NAME, 'p')
sleep(2)
print(text1.text)
chrome_driver.quit()
