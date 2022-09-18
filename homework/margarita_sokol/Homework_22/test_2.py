# Второй тест
# https://demoqa.com/menu#
# выбрать Main item2 ->
# SUB SUB List -> Sub Sub Item 2

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test2(driver_chrome):
    driver_chrome.get('https://demoqa.com/menu#')
    driver_chrome.maximize_window()
    sleep(3)
    main_item2 = driver_chrome.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(driver_chrome).move_to_element(main_item2).perform()
    sub_element = driver_chrome.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(driver_chrome).move_to_element(sub_element).perform()
    sub_sub_item2 = driver_chrome.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(driver_chrome).move_to_element(sub_sub_item2).perform()
