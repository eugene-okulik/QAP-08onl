# Задание
# Напишите программу,
# которая зайдет на сайт http://automationpractice.com/,
# кликнет по ссылке Contact us,
# полностью заполнит форму (кроме аплода файла) и нажмет Send.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.get("http://automationpractice.com/")
sleep(5)

element = driver.find_element(By.ID, "contact-link")
element.click()

element = driver.find_element(By.ID, "uniform-id_contact")
element.click()
sleep(3)
select = Select(driver.find_element(By.ID, "id_contact"))
select.select_by_value("2")

element = driver.find_element(By.ID, "email")
element.click()
element.send_keys("kirylchyk@gmail.com")

element = driver.find_element(By.ID, "id_order")
element.click()
element.send_keys("Order01")

element = driver.find_element(By.ID, "message")
element.click()
element.send_keys("Order Request")

element = driver.find_element(By.ID, "submitMessage")
element.click()
sleep(5)

driver.quit()
