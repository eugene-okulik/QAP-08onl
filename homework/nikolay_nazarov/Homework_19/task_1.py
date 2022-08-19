from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://automationpractice.com/")
chrome_driver.maximize_window()

contact_us = chrome_driver.find_element(By.ID, 'contact-link')
contact_us.click()

form1 = chrome_driver.find_element(By.ID, 'id_contact')
form1.click()

select = Select(chrome_driver.find_element(By.NAME, 'id_contact'))
select.select_by_value("1")

form2 = chrome_driver.find_element(By.ID, 'email')
form2.send_keys("nikolaynazarovvv216@gmail.com")

form3 = chrome_driver.find_element(By.ID, 'id_order')
form3.send_keys("11")

form4 = chrome_driver.find_element(By.ID, 'message')
form4.send_keys("Want to buy shorts")

file_to_upload = chrome_driver.find_element(By.ID, 'fileUpload')
file_to_upload.send_keys(r"D:\sometext.txt")

button = chrome_driver.find_element(By.ID, 'submitMessage')
button.click()

text = chrome_driver.find_element(By.ID, 'center_column')
test_in_green_space = text.find_element(By.TAG_NAME, 'p')
print(test_in_green_space.text)
chrome_driver.quit()
