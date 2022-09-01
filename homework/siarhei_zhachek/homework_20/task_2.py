from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.set_window_size(760, 1080)

driver.get('https://demoqa.com/automation-practice-form')

firstname = driver.find_element(By.ID, 'firstName')
firstname.send_keys('Alex')

lastname = driver.find_element(By.ID, 'lastName')
lastname.send_keys('Ivanov')

email = driver.find_element(By.ID, 'userEmail')
email.send_keys('Ivanov@mail.com')

gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
gender.click()

phone = driver.find_element(By.ID, 'userNumber')
phone.send_keys('9319129746')

subjects = driver.find_element(By.XPATH, '//div[@class="subjects-auto-complete__input"]/input')
subjects.send_keys('Math')
subjects.send_keys(Keys.ENTER)
subjects.send_keys('Computer Science')
subjects.send_keys(Keys.ENTER)
subjects.send_keys('Economics')
subjects.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

hobbies = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
hobbies.click()
hobbies2 = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
hobbies2.click()

add_file = driver.find_element(By.ID, "uploadPicture")
add_file.send_keys('f:/test_1.txt')

address = driver.find_element(By.ID, 'currentAddress')
address.send_keys('Daresi No 2, Daresi Rd')

date = driver.find_element(By.ID, 'dateOfBirthInput')
date.click()
date_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
date_month.select_by_value('6')
date_years = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
date_years.select_by_value('1990')
date_dey = driver.find_element(By.CLASS_NAME, 'react-datepicker__day--025')
date_dey.click()

state = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
state.send_keys('Uttar Pradesh')
state.send_keys(Keys.ENTER)

city = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
city.send_keys('Agra')
city.send_keys(Keys.ENTER)

sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

submit_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
submit_button.click()

sleep(5)

driver.quit()
