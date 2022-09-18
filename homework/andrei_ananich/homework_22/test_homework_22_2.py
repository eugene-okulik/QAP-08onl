# https://demoqa.com/menu#
# выбрать Main item2 -> SUB SUB List -> Sub Sub Item 2 -
# здесь никакого ассерта не получится сделать

"""module"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test2(chrome_driver):
    """module"""
    chrome_driver.get('https://demoqa.com/menu#')
    chrome_driver.maximize_window()
    sleep(3)
    main_item2 = chrome_driver.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(chrome_driver).move_to_element(main_item2).perform()
    sub_sub_list = chrome_driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(chrome_driver).move_to_element(sub_sub_list).perform()
    sub_sub_item2 = chrome_driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(chrome_driver).move_to_element(sub_sub_item2).perform()
