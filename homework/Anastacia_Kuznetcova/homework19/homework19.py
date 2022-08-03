from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
Chrome_driver = webdriver.Chrome(service=serv)
Chrome_driver.maximize_window()
Chrome_driver.get('http://automationpractice.com/index.php')
element = Chrome_driver.find_element(By.ID, "contact-link")
element.click()
element = Chrome_driver.find_element(By.ID, "uniform-id_contact")
element.click()
select = Select(Chrome_driver.find_element(By.ID, "id_contact"))
select.select_by_value("2")
element = Chrome_driver.find_element(By.ID, "email")
element.click()
element.send_keys('stassia92@mail.ru')
element = Chrome_driver.find_element(By.ID, "id_order")
element.click()
element.send_keys(5893272)
upload = Chrome_driver.find_element(By.ID, "fileUpload")
element.click()
text_input = Chrome_driver.find_element(By.XPATH, "//input[@type='file']")
text_input.send_keys("D:/dz/homework/Anastacia_Kuznetcova/img/results.txt.txt")
element = Chrome_driver.find_element(By.ID, "message")
element.click()
element.send_keys("Домашка 19")
sleep(3)
element = Chrome_driver.find_element(By.ID, "submitMessage")
element.click()
text = Chrome_driver.find_element(By.CSS_SELECTOR, "#center_column > p").text
print(text)
