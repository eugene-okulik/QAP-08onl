from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument('start-maximized')
chrome_driver = webdriver.Chrome(options=options)

first_name = 'Tatiana'
last_name = 'Molofei'
email = 'tmolofei@yandex.by'
male, female, other = 0, 1, 2
mobile = '804458371700'
year_of_birth = 1988
month_of_birth = 12
day_of_birth = 18
subject = "English"
sports, reading, music = 3, 4, 5
current_address = 'Priluki, Mayskaya, 10'


def filling_practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')

    first_name_fill = driver.find_element(By.XPATH, '//input[@id="firstName"]')
    first_name_fill.send_keys(first_name)

    last_name_fill = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    last_name_fill.send_keys(last_name)

    email_fill = driver.find_element(By.ID, 'userEmail')
    email_fill.send_keys(email)

    gender_fill = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
    gender_fill[female].click()

    # The below code is not working and I don't know why
    # gender_fill = driver.find_element(By.XPATH, '//input[@class="custom-control-input"][@value="Female"]')
    # gender_fill.click()

    mobile_fill = driver.find_elements(By.XPATH, '//input[@class=" mr-sm-2 form-control"]')
    mobile_fill[2].send_keys(mobile)
    if len(mobile) != 10 or mobile.isdigit() is False:
        print("Error. The phone number must be 10 digits.")

    date_of_birth_fill = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_fill.click()
    month_fill = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    month_fill.select_by_value(f'{month_of_birth-1}')
    year_fill = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    year_fill.select_by_value(f'{year_of_birth}')
    day_of_birth_fill = driver.find_element(By.CLASS_NAME, f'react-datepicker__day--0{day_of_birth}')
    day_of_birth_fill.click()

    subject_fill = driver.find_element(By.XPATH, '//div[@class="subjects-auto-complete__input"]/input')
    subject_fill.send_keys(subject)
    subject_fill.send_keys(Keys.ENTER)

    hobbies_fill = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
    hobbies_fill[sports].click()

    current_address_fill = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')
    current_address_fill.send_keys(current_address)

    file_uploading = driver.find_element(By.ID, 'uploadPicture').find_element(By.XPATH, "//input[@type='file']")
    file_uploading.send_keys("/home/tm/Downloads/me.jpeg")
    file_uploading.submit()


filling_practice_form(chrome_driver)
