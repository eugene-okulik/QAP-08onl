from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(executable_path="D:\\driver\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service)


def complete_form(driver):
    """This function fills and submits a form of user's info"""
    driver.get('https://demoqa.com/automation-practice-form')
    driver.maximize_window()

    name = driver.find_element(By.CLASS_NAME, 'form-control')
    name.send_keys('Artyom')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    last_name.send_keys("Zabello")

    email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')
    email.send_keys('artyomzabello@yandex.by')

    buttons_and_checkboxes = chrome_driver.find_elements(By.XPATH,
                                                         '//label[@class="custom-control-label"]')

    buttons_and_checkboxes[0].click()
    phone = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mobile Number"]')
    phone.send_keys('80295671123')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, "dateOfBirthInput").click()

    select_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    select_month.select_by_value("4")
    select_year = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    select_year.select_by_value("1999")
    driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012').click()

    buttons_and_checkboxes[4].click()
    send_picture = driver.find_element(By.CLASS_NAME, 'form-control-file')
    send_picture.send_keys('D:\\logs\\photo.png')
    address = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')
    address.send_keys("15, Lenin Avenue")
    address.submit()
    sleep(2)
    driver.quit()


complete_form(chrome_driver)
