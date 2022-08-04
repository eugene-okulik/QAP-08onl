from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv = Service(executable_path="C:\\Scripts\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=serv)
chrome_driver.get("https://automationpractice.com/")
chrome_driver.maximize_window()

contact_us = chrome_driver.find_element(By.ID, 'contact-link')
contact_us.click()

form1 = chrome_driver.find_element(By.ID, 'id_contact')
form1.click()

select = Select(chrome_driver.find_element(By.NAME, 'id_contact'))
select.select_by_value("1")

form2 = chrome_driver.find_element(By.ID, 'email')
form2.send_keys("lanselap1488@gmail.com")

form3 = chrome_driver.find_element(By.ID, 'id_order')
form3.send_keys("11")

form4 = chrome_driver.find_element(By.ID, 'message')
form4.send_keys("Want to buy shorts")

upload_file = chrome_driver.find_element(By.ID, 'fileUpload')
upload_file.send_keys("D:\\logs\\logs.txt")

button = chrome_driver.find_element(By.ID, 'submitMessage')
button.click()

text = chrome_driver.find_element(By.ID, 'center_column')
text1 = text.find_element(By.TAG_NAME, 'p')
print(text1.text)
chrome_driver.quit()
