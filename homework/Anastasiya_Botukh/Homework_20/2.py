from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('window-size=760,1080')
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/automation-practice-form")

first_name_field = driver.find_element(By.ID, "firstName")
first_name_field.click()
first_name_field.send_keys("Anastasiya")

last_name_field = driver.find_element(By.ID, "lastName")
last_name_field.click()
last_name_field.send_keys("Botukh")

email_field = driver.find_element(By.ID, "userEmail")
email_field.click()
email_field.send_keys("aaisatsana18@gmail.com")

# gender_field = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
# gender_field[1].click()

number_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mobile Number"]')
number_field.click()
number_field.send_keys('80298896287')

# birthday_field = driver.find_element(By.ID, "dateOfBirthInput")
# birthday_field.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID, "dateOfBirthInput").click()
year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
year_select.select_by_value("1998")
month_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
month_select.select_by_value("9")
driver.find_element(By.CLASS_NAME, "react-datepicker__day--006").click()

subjects_field = driver.find_element(By.XPATH,
                                     '//div[@class="subjects-auto-complete__input"]/input')
subjects_field.send_keys("English, ")
subjects_field.send_keys("Automation testing, ")
subjects_field.send_keys("Stretching")
subjects_field.send_keys(Keys.ENTER)

hobbies_field = driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_field[4].click()

picture_field = driver.find_element(By.ID, "uploadPicture")
picture_input = driver.find_element(By.XPATH, "//input[@type='file']")
picture_input.send_keys("/Users/aisatsana/Downloads/TMS.jpg")

current_address_field = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Current Address"]')
current_address_field.send_keys("Belarus, Minsk")
current_address_field.submit()

state_field = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
state_field.send_keys('NCR')
state_field.send_keys(Keys.ENTER)

city_field = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
city_field.send_keys('Agra')
city_field.send_keys(Keys.ENTER)

sleep(3)

driver.quit()
