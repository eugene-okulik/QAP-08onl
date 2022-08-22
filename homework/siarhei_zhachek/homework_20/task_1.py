from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def checkboxes():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demoqa.com/checkbox')

    button = driver.find_element(By.XPATH, '//button[@title="Expand all"]')
    button.click()

    checkbox = driver.find_elements(By.XPATH, '//span[@class="rct-checkbox"]')
    for i in checkbox:
        i.click()
        break

    sleep(3)
    driver.quit()


checkboxes()
