from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://demoqa.com/automation-practice-form")
chrome_driver.maximize_window()

first_name_placeholder = chrome_driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]')
first_name_placeholder.send_keys("Николай")

second_name_placeholder = chrome_driver.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')
second_name_placeholder.send_keys("Назаров")

email_placeholder = chrome_driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]')
email_placeholder.send_keys("nikolaynazarovvv216@gmail.com")

gender_radio_button = chrome_driver.find_element(By.CLASS_NAME, 'custom-control')
gender_radio_button.click()

email_placeholder = chrome_driver.find_element(By.ID, 'userNumber')
email_placeholder.send_keys("9964410394")

day_of_birth_placeholder = chrome_driver.find_element(By.ID, 'dateOfBirthInput')
day_of_birth_placeholder.send_keys("04 December 1994")

select_year = Select(chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
select_year.select_by_value("1994")

day_4 = chrome_driver.find_element(By.CLASS_NAME, "react-datepicker__day--004")
day_4.click()

day_of_birth_placeholder = chrome_driver.find_element(By.ID, 'subjectsInput')
day_of_birth_placeholder.send_keys("Math")
day_of_birth_placeholder.send_keys(Keys.ENTER)

sports_checkbox = chrome_driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
sports_checkbox.click()

reading_checkbox = chrome_driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
reading_checkbox.click()

music_checkbox = chrome_driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
music_checkbox.click()

upload_picture = chrome_driver.find_element(By.ID, "uploadPicture")
upload_picture.send_keys(r"D:\1.jpg")

current_address_placeholder = chrome_driver.find_element(By.ID, 'currentAddress')
current_address_placeholder.send_keys("Mytisci, st. Razvedchika Abelia, h. 1")

select_state = chrome_driver.find_element(By.CSS_SELECTOR, 'div[id="stateCity-wrapper"] > '
                                                           'div:nth-child(2) > div')
select_state.click()
state_input = chrome_driver.find_element(By.ID, 'react-select-3-input')
state_input.send_keys("NCR")
state_input.send_keys(Keys.ENTER)

select_city = chrome_driver.find_element(By.CSS_SELECTOR, 'div[id="stateCity-wrapper"] > '
                                                          'div:nth-child(3) > div')
select_city.click()
city_input = chrome_driver.find_element(By.ID, 'react-select-4-input')
city_input.send_keys("Noi")
city_input.send_keys(Keys.ENTER)

submit_button = chrome_driver.find_element(By.ID, "submit")
submit_button.click()

button_in_modal_window = chrome_driver.find_element(By.ID, "closeLargeModal")
button_in_modal_window.click()

chrome_driver.quit()
