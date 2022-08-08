# Задание 2
# Заполнить эту форму
# https://demoqa.com/automation-practice-form

import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
# // options=options)

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# driver = webdriver.Safari()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(3)

driver.execute_script("""
    var l = document.getElementById("fixedban").remove();
 """)

fe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))
fe.send_keys("Varvara")

ln = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lastName")))
ln.send_keys("Kirylchyk")

userEmail_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located //
                                                    ((By.ID, "userEmail")))
userEmail_element.send_keys("kirylchyk@gmail.com")

driver.switch_to.default_content()
gender_element = driver.find_element(By.ID, "gender-radio-2")
# gender_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable
# //((By.ID, "gender-radio-2")))

driver.execute_script('arguments[0].scrollIntoView(true);', gender_element)
driver.execute_script("arguments[0].click();", gender_element)

# action = webdriver.common.action_chains.ActionChains(driver)
# action.move_to_element_with_offset(gender_element, -3, -3)
# action.click()
# action.perform()
# time.sleep(5)
# gender_element.click()

time.sleep(3)
userNumber_element = driver.find_element(By.ID, "userNumber")
userNumber_element.click()
userNumber_element.send_keys("123")

driver.execute_script('arguments[0].scrollIntoView(true);', userNumber_element)
driver.execute_script("arguments[0].click();", userNumber_element)

time.sleep(3)
date_of_birth_fill = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth_fill.click()

select_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
select_month.select_by_value("10")
select_year = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
select_year.select_by_value("1988")
driver.find_element(By.CLASS_NAME, 'react-datepicker__day--006').click()

time.sleep(3)

subject_element = driver.find_element(By.XPATH,
                                        '//div[@class="subjects-auto-complete__input"]/input')
subject_element.click()
subject_element.send_keys("Question")

time.sleep(3)

# hobby_element = driver.find_element(By.CLASS_NAME, "hobbies-checkbox-3")
# hobby_element.click()

# time.sleep(3)

address_element = driver.find_element(By.ID, "currentAddress")
address_element.click()
address_element.send_keys("City")

time.sleep(3)

driver.execute_script('arguments[0].scrollIntoView(true);', address_element)
driver.execute_script("arguments[0].click();", address_element)

# state_element = Select(driver.find_element(By.ID, "state"))
# state_element.select_by_index(2)

# time.sleep(3)

submit_element = driver.find_element(By.ID, "submit")
submit_element.click()
