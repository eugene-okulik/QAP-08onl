from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument('window-size=2048,1080')
driver = webdriver.Chrome(options=options)

driver.get('http://automationpractice.com/')
click_button = driver.find_element(By.ID, "contact-link")
click_button.click()

field_select = driver.find_element(By.ID, "uniform-id_contact")
field_select.click()
field_select1 = Select(driver.find_element(By.ID, "id_contact"))
field_select1.select_by_value("1")

field_email = driver.find_element(By.ID, "email")
field_email.click()
field_email.send_keys("aaisatsana18@gmail.com")

field_order = driver.find_element(By.ID, "id_order")
field_email.click()
field_order.send_keys("12345")

field_upload = driver.find_element(By.ID, "fileUpload")
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys("/Users/aisatsana/Desktop/homework_19.txt")
sleep(2)

field_message = driver.find_element(By.ID, "message")
field_message.click()
field_message.send_keys('Is it possible to try on jeans?')
sleep(3)

field_submit = driver.find_element(By.ID, "submitMessage")
field_submit.click()
success_message = driver.find_element(By.ID, "center_column").find_element(By.TAG_NAME, "p").text
print(success_message)

driver.quit()
