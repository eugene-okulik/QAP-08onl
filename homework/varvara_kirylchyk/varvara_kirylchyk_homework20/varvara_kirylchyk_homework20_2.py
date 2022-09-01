"""System module."""
# Задание 2
# Заполнить эту форму
# https://demoqa.com/automation-practice-form

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument('window-size=960,640')
chrome_driver = webdriver.Chrome(options=options)

FIRST_NAME = 'Varvara'
LAST_NAME = 'Kirylchyk'
EMAIL = 'varvara.kirylchyk@yandex.ru'
male, female, other = 0, 1, 2
MOBILE = '1123456789'
YEAR_OF_BIRTH = 1988
MONTH_OF_BIRTH = 11
DAY_OF_BIRTH = 10
SUBJECT = "Question"
sports, reading, music = 3, 4, 5
ADDRESS = 'City'
STATE = "ABC"
CITY = 'Minsk'


def filling_practice_form(driver):
    """A dummy docstring."""
    driver.get('https://demoqa.com/automation-practice-form')
    driver.execute_script("""
        var l = document.getElementById("fixedban").remove();
     """)

    first_name_fill = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name_fill.send_keys(FIRST_NAME)

    last_name_fill = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    last_name_fill.send_keys(LAST_NAME)

    email_fill = driver.find_element(By.ID, 'userEmail')
    email_fill.send_keys(EMAIL)

    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 1080)")

    gender_fill = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
    gender_fill[female].click()

    mobile_fill = driver.find_elements(By.XPATH, '//input[@class=" mr-sm-2 form-control"]')
    mobile_fill[2].send_keys(MOBILE)
    if len(MOBILE) != 10 or MOBILE.isdigit() is False:
        print("Error. The phone number must be 10 digits.")

    driver.execute_script("window.scrollTo(0, 1080)")

    date_of_birth_fill = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_fill.click()
    month_fill = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    month_fill.select_by_value(f'{MONTH_OF_BIRTH-1}')
    year_fill = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    year_fill.select_by_value(f'{YEAR_OF_BIRTH}')
    day_fill = driver.find_element(By.CLASS_NAME, f'react-datepicker__day--0{DAY_OF_BIRTH}')
    day_fill.click()

    time.sleep(3)

    subject_fill = driver.find_element(By.XPATH,
                                        '//div[@class="subjects-auto-complete__input"]/input')
    subject_fill.send_keys(SUBJECT)
    subject_fill.send_keys(Keys.ENTER)

    driver.execute_script('arguments[0].scrollIntoView(true);', subject_fill)
    driver.execute_script("arguments[0].click();", subject_fill)
    time.sleep(3)

    hobbies_fill = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
    hobbies_fill[music].click()

    current_address_fill = driver.find_element(By.CSS_SELECTOR,
                                                'textarea[placeholder="Current Address"]')
    current_address_fill.send_keys(ADDRESS)

    time.sleep(3)

    file_uploading = driver.find_element(By.ID, 'uploadPicture')
    file_uploading = file_uploading.find_element(By.XPATH, "//input[@type='file']")
    file_uploading.send_keys("/Downloads/cats.jpeg")
    file_uploading.submit()

    state = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    state.send_keys(STATE)
    state.send_keys(Keys.ENTER)

    # city = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    # city.send_keys(CITY)
    # city.send_keys(Keys.ENTER)

filling_practice_form(chrome_driver)
