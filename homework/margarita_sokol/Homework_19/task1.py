# Напишите программу, которая зайдет на сайт
# http://automationpractice.com/, кликнет по ссылке Contact us,
# полностью заполнит форму (кроме аплода файла) и нажмет Send.
# Заполните также поле аплода файла, т.е. приаттачьте файл.
# После отправки вам будет отображено, что все оправлено успешно.
# Получите со страницы тот текст, который будет находиться
# в зеленом прямоугольнике и распечатайте его.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


service = Service(executable_path='chromedriver.exe')


options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)


driver.get('http://automationpractice.com/')
contact_us_button = driver.find_element(By.ID, 'contact-link')
contact_us_button.click()


heading = Select(driver.find_element(By.ID, "id_contact"))
heading.select_by_value('2')


email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('test@mail.com')


order_reference = driver.find_element(By.ID, 'id_order')
order_reference.send_keys('15161718')

attach_file = driver.find_element(By.XPATH, "//input[@type='file']")
attach_file.send_keys('C:/Users/Марго/Desktop/TMS/myfile.txt')

massage = driver.find_element(By.ID, 'message')
massage.send_keys('Test, test, test.')

send_button = driver.find_element(By.NAME, 'submitMessage')
send_button.click()

message_text = driver.find_element(By.ID, 'center_column')
message_text = message_text.find_element(By.TAG_NAME, "P")
print(message_text.text)

sleep(3)

driver.quit()
