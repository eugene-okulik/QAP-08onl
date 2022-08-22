# Заполнить эту форму
# https://demoqa.com/automation-practice-form

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


service = Service(executable_path='../Homework_21/chromedriver.exe')
chrome_driver = webdriver.Chrome(service=service)


def fill_in_the_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    driver.maximize_window()

    name_form = driver.find_element(By.ID, 'firstName')
    name_form.send_keys('Margarita')


    last_name_form = driver.find_element(By.ID, 'lastName')
    last_name_form.send_keys('Sokol')


    email_form = driver.find_element(By.ID, 'userEmail')
    email_form.send_keys('test@mail.com')


    gender_checkboxes = driver.find_elements(By.XPATH,
                                             '//label[@class="custom-control-label"]')
    gender_checkboxes[1].click()


    phone_form = driver.find_element(By.ID, 'userNumber')
    phone_form.send_keys('6254381221')


    date_of_birth_form = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth_form.click()

    select_month = Select(driver.find_element(By.CLASS_NAME,
                                              'react-datepicker__month-select'))
    select_month.select_by_value("7")

    select_year = Select(driver.find_element(By.CLASS_NAME,
                                             'react-datepicker__year-select'))
    select_year.select_by_value("1995")

    select_day = driver.find_element(By.CLASS_NAME,  'react-datepicker__day--014')
    select_day.click()


    subject_form = driver.find_element(By.XPATH,
                                       '//div[@class="subjects-auto-complete__input"]/input')
    subject_form.send_keys('History')
    subject_form.send_keys(Keys.ENTER)


    hobbies_checkboxes = driver.find_elements(By.XPATH,
                                              '//label[@class="custom-control-label"]')
    hobbies_checkboxes[4].click()


    address_form = driver.find_element(By.CSS_SELECTOR,
                                       'textarea[placeholder="Current Address"]')
    address_form.send_keys('Belsrus, Minsk, Spilevskogo 67')
    address_form.submit()


    file_uploading = driver.find_element(By.ID, 'uploadPicture')
    file_uploading = file_uploading.find_element(By.XPATH, "//input[@type='file']")
    file_uploading.send_keys('C:/Users/Марго/Desktop/TMS/myfile.txt')
    file_uploading.submit()

    sleep(15)
    driver.quit()


fill_in_the_form(chrome_driver)
