from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)

driver.get('http://automationpractice.com/index.php')

element = driver.find_element(By.ID, "contact-link")
element.click()

element = driver.find_element(By.ID, "uniform-id_contact")
element.click()
select = Select(driver.find_element(By.ID, "id_contact"))
select.select_by_value("2")

element = driver.find_element(By.ID, "email")
element.click()
element.send_keys('tmolofei@yandex.by')

element = driver.find_element(By.ID, "id_order")
element.click()
element.send_keys(12358)

# element = driver.find_element(By.ID, "uniform-fileUpload")
# element.click()
# element = driver.find_element(By.XPATH, "//div[@class='uploader']//input[@type=‘file’]")
# element.send_keys(r"C:\Users\Hello.txt")
# element.click()

element = driver.find_element(By.ID, "message")
element.click()
element.send_keys('Hello, Eugene')

element = driver.find_element(By.ID, "submitMessage")
element.click()

message = driver.find_element(By.ID, "center_column").find_element(By.TAG_NAME, "P").text
print(message)
