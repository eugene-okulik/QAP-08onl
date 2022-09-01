from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_two(driver):
    driver.get('https://demoqa.com/menu#')
    main_item_2 = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(driver).move_to_element(main_item_2).perform()
    sub_sub_list = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(driver).move_to_element(sub_sub_list).perform()
    sub_sub_item_2 = driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(driver).move_to_element(sub_sub_item_2).perform()
