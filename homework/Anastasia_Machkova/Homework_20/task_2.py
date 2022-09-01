from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='chromedriver.exe')

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)


driver.get('https://demoqa.com/automation-practice-form')
first_name = driver.find_element(By.ID, 'firstName')
first_name.send_keys('Anastasia')

last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('Machkova')

email_address = driver.find_element(By.ID, 'userEmail')
email_address.send_keys('nastya.machkova@gmail.com')

gender = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
gender[1].click()

mobile_number = driver.find_element(By.ID, 'userNumber')
mobile_number.send_keys('3754456777')

date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth.click()
select_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
select_month.select_by_value('9')

select_year = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
select_year.select_by_value('1998')
driver.find_element(By.CLASS_NAME, 'react-datepicker__day--003').click()

subject = driver.find_element(By.XPATH, '//div[@class="subjects-auto-complete__input"]/input')
subject.send_keys('English')
subject.send_keys(Keys.ENTER)

hobbies_sport = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_sport[4].click()

upload_file = driver.find_element(By.ID, 'uploadPicture')
attach_file = driver.find_element(By.XPATH, "//input[@type='file']")
attach_file.send_keys('C:/Users/a.machkova.MACHKOVA-T490/Desktop/myfile.txt')

current_address = driver.find_element(By.ID, 'currentAddress')
current_address.send_keys('Minsk, Rotmistrova 36-1-108')

select_state = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
select_state.send_keys('Uttar Pradesh')
select_state.send_keys(Keys.ENTER)

select_city = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
select_city.send_keys('Agra')
select_state.send_keys(Keys.ENTER)

Successfully_send = driver.find_element(By.XPATH, '//div[@id="example-modal-sizes-title-lg"]')
print(Successfully_send.text)

sleep(5)
driver.quit()
