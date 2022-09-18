from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

serv = Service(executable_path='chromedriver.exe')
Chrome_driver = webdriver.Chrome()
Chrome_driver.set_window_size(760, 1080)
Chrome_driver.get("https://demoqa.com/automation-practice-form")


first_name_field = Chrome_driver.find_element(By.ID, "firstName")
first_name_field.send_keys('Vadim')

last_name_field = Chrome_driver.find_element(By.ID, "lastName")
last_name_field.send_keys('Zhenevsky')

email_field = Chrome_driver.find_element(By.ID, "userEmail")
email_field.send_keys('vadim@mail.com')

gender_form = Chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
gender_form[0].click()

mobile_number_field = Chrome_driver.find_element(By.ID, "userNumber")
mobile_number_field.send_keys('1297160245')

Date_of_Birth_field = Chrome_driver.find_element(By.ID, "dateOfBirthInput")
Date_of_Birth_field.click()

month_select = Select(Chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
month_select.select_by_value("0")

year_select = Select(Chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
year_select.select_by_value("1986")

day_select = Chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__day--020')
day_select.click()

subject = Chrome_driver.find_element(By.ID, 'subjectsInput')
subject.send_keys('Chemistry')
subject.send_keys(Keys.ENTER)

hobbies_sport = Chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_sport[3].click()

hobbies_reading = Chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_reading[4].click()

hobbies_music = Chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_music[5].click()

send_picture = Chrome_driver.find_element(By.CLASS_NAME, 'form-control-file')
send_picture.send_keys('C:/Users/v.zhenevskiy/Desktop/УЧЕБА/FOTO.jpg')

Current_Address_field = Chrome_driver.find_element(By.ID, "currentAddress")
Current_Address_field.send_keys('Minsk, Esenina str.')

state_form = Chrome_driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
state_form.send_keys('NCR')
state_form.send_keys(Keys.ENTER)

city_form = Chrome_driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
city_form.send_keys('Delhi')
city_form.send_keys(Keys.ENTER)

submit = Chrome_driver.find_element(By.CLASS_NAME, 'btn-primary')
submit.click()
