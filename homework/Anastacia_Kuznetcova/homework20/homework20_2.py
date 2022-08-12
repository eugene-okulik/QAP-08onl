from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
chrome_driver = webdriver.Chrome(service=serv)
chrome_driver.set_window_size(760, 1080)
chrome_driver.get('https://demoqa.com/automation-practice-form')
name_form = chrome_driver.find_element(By.ID, "firstName")
name_form.send_keys('Anastacia')
lastname_form = chrome_driver.find_element(By.ID, "lastName")
lastname_form.send_keys('Kuznetcova')
email_form = chrome_driver.find_element(By.ID, "userEmail")
email_form.send_keys('stassia92@mail.ru')
gender_form = chrome_driver.find_elements(By.XPATH,
                                          '//label[@class="custom-control-label"]')
gender_form[1].click()
phone_form = chrome_driver.find_element(By.ID, "userNumber")
phone_form.send_keys('5554455000')
date_of_birth = chrome_driver.find_element(By.ID, "dateOfBirthInput")
date_of_birth.click()
choose_month = Select(chrome_driver.find_element(By.CLASS_NAME,
                                                 'react-datepicker__month-select'))
choose_month.select_by_value("1")
choose_year = Select(chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
choose_year.select_by_value("1992")
choose_day = chrome_driver.find_element(By.CLASS_NAME, 'react-datepicker__day--031')
choose_day.click()
subject_form = chrome_driver.find_element(By.XPATH,
                                          '//div[@class="subjects-auto-complete__input"]/input')
subject_form.send_keys('Computer Science')
subject_form.send_keys(Keys.ENTER)
hobbies_form = chrome_driver.find_elements(By.XPATH, '//label[@class="custom-control-label"]')
hobbies_form[5].click()
file = chrome_driver.find_element(By.ID, 'uploadPicture')
file = file.find_element(By.XPATH,
                         "//input[@type='file']")
file.send_keys("D:/dz/homework/Anastacia_Kuznetcova/img/tumblr_mu7oabGB6n1ssqskzo1_r1_500.png")
address_form = chrome_driver.find_element(By.CSS_SELECTOR,
                                          'textarea[placeholder="Current Address"]')
address_form.send_keys('Israel, Akko, Nehoshet 3')
state_form = chrome_driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
state_form.send_keys('NCR')
state_form.send_keys(Keys.ENTER)
city_form = chrome_driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
city_form.send_keys('Delhi')
city_form.send_keys(Keys.ENTER)
submit = chrome_driver.find_element(By.CLASS_NAME, 'btn-primary')
submit.click()
