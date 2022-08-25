from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


def test_1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    goods = driver.find_elements(By.CLASS_NAME, 'hrefch')
    goods[0].send_keys(Keys.LEFT_CONTROL, Keys.ENTER)
    win = driver.window_handles
    driver.switch_to.window(win[1])
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(win[0])
    driver.find_element(By.ID, 'cartur').click()
    cart = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert "Samsung galaxy s6" in cart.text


def test_2(driver):
    driver.get('https://demoqa.com/menu#')
    sleep(1)
    main_item_2 = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(driver).move_to_element(main_item_2).perform()
    sub_list = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(driver).move_to_element(sub_list).perform()
    sub_item_2 = driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(driver).move_to_element(sub_item_2).perform()


def test_3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.find_element(By.ID, 'promptexample').click()
    Alert(driver).send_keys('Homework22')
    Alert(driver).accept()
    assert 'Homework22' in driver.find_element(By.ID, 'promptreturn').text
