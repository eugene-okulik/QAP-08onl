from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

service = Service(executable_path='chromedriver.exe')
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def complete_form(driver):

    driver.get('https://demoqa.com/automation-practice-form')
    driver.maximize_window()

    name = driver.find_element(By.CLASS_NAME, 'form-control')
    name.send_keys('Sergey')

    l_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    l_name.send_keys("Wolk")

    eml = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')
    eml.send_keys('svwolk1991@gmail.com')

    buttons_and_checkboxes = driver.find_elements(By.XPATH,
                                                         '//label[@class="custom-control-label"]')

    buttons_and_checkboxes[0].click()
    phone = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mobile Number"]')
    phone.send_keys('80441773396')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, "dateOfBirthInput").click()

    sel_month = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    sel_month.select_by_value("2")
    sel_year = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    sel_year.select_by_value("1991")
    driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012').click()

    buttons_and_checkboxes[4].click()
    #send_picture = driver.find_element(By.CLASS_NAME, 'form-control-file')
    #send_picture.driver.findElement(By.id("photo.png")).sendKeys("D:\\photo.png")
    address = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')
    address.send_keys("72, Sharangovich street")
    address.submit()
    sleep(2)
    driver.quit()

complete_form(driver)
