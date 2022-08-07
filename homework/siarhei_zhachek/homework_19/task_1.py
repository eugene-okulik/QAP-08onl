from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


options = Options()
options.add_argument('start-maximized')


service = Service(executable_path="c:/Users/Admin/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


driver.get('http://automationpractice.com/')
contact_us_button = driver.find_element(By.ID, 'contact-link')
contact_us_button.click()


email = driver.find_element(By.ID, "email")
email.send_keys('my@mail.com')


order = driver.find_element(By.ID, "id_order")
order.send_keys('1254780')


heading = Select(driver.find_element(By.ID, "id_contact"))
heading.select_by_value("2")


massage = driver.find_element(By.ID, "message")
massage.send_keys('Hello test!')


file = driver.find_element(By.XPATH, "//input[@type='file']")
file.send_keys('c:/Users/Admin/Downloads/1.txt.txt')
sleep(3)


to_send = driver.find_element(By.ID, 'submitMessage')
to_send.click()


text = driver.find_element(By.ID, 'center_column')
text = text.find_element(By.TAG_NAME, "P")
print(text.text)
sleep(3)

driver.quit()
