# Заполнить эту форму
# https://demoqa.com/automation-practice-form

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                  "andrei_ananich\\selenium\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)
chrome_driver.set_window_size(760, 760)
chrome_driver.get('https://demoqa.com/automation-practice-form')
#chrome_driver.execute_script("document.body.style.zoom='67%'")

name_field = chrome_driver.find_element(By.ID, "firstName")
name_field.send_keys('Andrei')

lastname_field = chrome_driver.find_element(By.ID, "lastName")
lastname_field.send_keys('Ananich')

email_field = chrome_driver.find_element(By.ID, "userEmail")
email_field.send_keys('andrei.ananich@gmail.com')
sleep(2)

gender_field = chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
gender_field[0].click()

mobile_phone_field = chrome_driver.find_element(By.ID, "userNumber")
mobile_phone_field.send_keys('0123456789')

chrome_driver.execute_script("window.scrollTo(0, 600)")

date_of_birth_field = chrome_driver.find_element(By.ID, "dateOfBirthInput")
date_of_birth_field.click()
choose_month = Select(chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
choose_month.select_by_value("4")
choose_year = Select(chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
choose_year.select_by_value("1984")
choose_day = chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__day--029')
choose_day.click()

subject_field = chrome_driver.find_element(By.XPATH,
                                           '//div[@class="subjects-auto-complete__input"]/input')
subject_field.send_keys('Computer Science')
subject_field.send_keys(Keys.ENTER)
sleep(2)

hobbies_field = chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_field[5].click()

file_upload = chrome_driver.find_element(By.ID, 'uploadPicture')
file_upload = file_upload.find_element(By.XPATH, "//input[@type='file']")
file_upload.send_keys("C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                      "andrei_ananich\\homework_20\\test.jpg")

current_address_field = chrome_driver.find_element(By.CSS_SELECTOR,
                                                   'textarea[placeholder="Current Address"]')
current_address_field.send_keys('Belarus, Minsk')

state_form = chrome_driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
state_form.send_keys('NCR')
state_form.send_keys(Keys.ENTER)

city_form = chrome_driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
city_form.send_keys('Delhi')
city_form.send_keys(Keys.ENTER)
sleep(5)

submit = chrome_driver.find_element(By.CLASS_NAME, 'btn-primary')
submit.click()
