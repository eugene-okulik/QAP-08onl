from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

opt = Options()
opt.add_argument('window-size=760,1080')
service = Service(executable_path="D:\\driver\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service, options=opt)
chrome_driver.implicitly_wait(1)


def complete_form(driver):
    """This function fills and submits a form of user's info"""
    driver.get('https://demoqa.com/automation-practice-form')

    name = driver.find_element(By.CLASS_NAME, 'form-control')
    name.send_keys('Artyom')

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    last_name.send_keys("Zabello")

    email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')
    email.send_keys('artyomzabello@yandex.by')

    buttons_and_checkboxes = driver.find_elements(By.XPATH,
                                                  '//label[@class="custom-control-label"]')
    buttons_and_checkboxes[0].click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    phone = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mobile Number"]')
    phone.send_keys('80295671123')

    driver.find_element(By.ID, "dateOfBirthInput").click()
    select_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    select_month.select_by_value("4")
    select_year = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    select_year.select_by_value("1999")
    driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012').click()

    subject = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subject.send_keys("English")
    subject.send_keys(Keys.ENTER)

    buttons_and_checkboxes[4].click()
    send_picture = driver.find_element(By.CLASS_NAME, 'form-control-file')
    send_picture.send_keys('D:\\logs\\photo.png')
    address = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')
    address.send_keys("15, Lenin Avenue")

    state = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    state.send_keys('NCR')
    state.send_keys(Keys.ENTER)

    city = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    city.send_keys('Delhi')
    city.send_keys(Keys.ENTER)
    address.submit()
    sleep(2)
    driver.quit()


complete_form(chrome_driver)
