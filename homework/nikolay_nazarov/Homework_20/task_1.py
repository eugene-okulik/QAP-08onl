from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://demoqa.com/checkbox")
chrome_driver.maximize_window()

home_checkbox = chrome_driver.find_element(By.CSS_SELECTOR, '.rct-text .rct-collapse')
home_checkbox.click()

desktop_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                              '.rct-node > ol > '
                                              'li:nth-child(1) > span > button')
desktop_checkbox.click()

documents_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                                '.rct-node > ol > '
                                                'li:nth-child(2) > span > button')
documents_checkbox.click()

downloads_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                                '.rct-node > ol > '
                                                'li:nth-child(3) > span > button')
downloads_checkbox.click()

notes_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                            '.rct-node > ol > li:nth-child(1) > ol > '
                                            'li:nth-child(1) .rct-checkbox')
notes_checkbox.click()

commands_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                               '.rct-node > ol > li:nth-child(1) > ol > '
                                               'li:nth-child(2) .rct-checkbox')
commands_checkbox.click()

workspace_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                                '.rct-node > ol > li:nth-child(2) > ol > '
                                                'li:nth-child(1) .rct-checkbox')
workspace_checkbox.click()

office_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                             '.rct-node > ol > li:nth-child(2) > ol > '
                                             'li:nth-child(2) .rct-checkbox')
office_checkbox.click()

word_file_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                                '.rct-node > ol > li:nth-child(3) > ol > '
                                                'li:nth-child(1) .rct-checkbox')
word_file_checkbox.click()

excel_file_checkbox = chrome_driver.find_element(By.CSS_SELECTOR,
                                                 '.rct-node > ol > li:nth-child(3) > ol > '
                                                 'li:nth-child(2) .rct-checkbox')
excel_file_checkbox.click()

chrome_driver.quit()
