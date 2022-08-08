from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

service = Service(executable_path='chromedriver.exe')
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('http://automationpractice.com')

cont = driver.find_element(By.ID, 'contact-link')
cont.click()

id_cont = driver.find_element(By.ID, 'id_contact')
id_cont.click()

sel = Select(driver.find_element(By.NAME, 'id_contact'))
sel.select_by_value("2")

eml = driver.find_element(By.ID, 'email')
eml.send_keys("svwolk1991@gmail.com")

order = driver.find_element(By.ID, 'id_order')
order.send_keys("11")

mess = driver.find_element(By.ID, 'message')
mess.send_keys("Hello!Selenium!")

up_f = driver.find_element(By.ID, 'fileUpload')
up_f.send_keys("C:\\file_log.txt")

mess = driver.find_element(By.ID, 'submitMessage')
mess.click()

link = driver.find_element(By.ID, 'center_column')
link2 = link.find_element(By.TAG_NAME, 'p')
print(link2, link)
driver.quit()
