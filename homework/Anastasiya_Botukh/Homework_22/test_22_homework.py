import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    sleep(2)
    driver.execute_script("window.scrollTo(800, 1000)")
    sleep(2)
    new_window = driver.find_element(By.XPATH,
                                     "//*[@id=\"tbodyid\"]/div[8]/div/div/h4/a")
    ActionChains(driver).move_to_element(new_window).\
        key_down(Keys.COMMAND).click(new_window).key_up(Keys.COMMAND).perform()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(8)"]').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script("window.scrollTo(0, -250)")
    cart = driver.find_element(By.ID, 'cartur')
    ActionChains(driver).double_click(cart).perform()
    cart_check = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert 'Sony vaio i5' in cart_check.text


def test_2(driver):
    driver.get('https://demoqa.com/menu#')
    main_item = driver.find_element(By.XPATH, '//*[@id=\"nav\"]/li[2]/a')
    ActionChains(driver).move_to_element(main_item).perform()
    sub_sub_list = driver.find_element(By.XPATH, '//*[@id=\"nav\"]/li[2]/ul/li[3]/a')
    ActionChains(driver).move_to_element(sub_sub_list).perform()
    sub_sub_item_2 = driver.find_element(By.XPATH, '//*[@id=\"nav\"]/li[2]/ul/li[3]/ul/li[2]/a')
    ActionChains(driver).move_to_element(sub_sub_item_2).perform()


def test_3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, 'promptexample').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).send_keys('hello')
    Alert(driver).accept()
    check_word = driver.find_element(By.ID, 'promptreturn')
    assert check_word.text == 'hello'
