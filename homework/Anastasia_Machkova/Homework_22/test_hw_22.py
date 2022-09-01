from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


def test_1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    sleep(2)
    new_tab = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=5"]')
    ActionChains(driver).move_to_element(new_tab).key_down(Keys.CONTROL).click(new_tab).\
        key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(5)"]').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart = driver.find_element(By.ID, 'cartur')
    ActionChains(driver).move_to_element(cart).click().perform()
    iphone = driver.find_element(By.XPATH, '//tbody[@id="tbodyid"]/tr/td[2]')
    assert "Iphone 6 32gb" in iphone.text


def test_2(driver):
    driver.get('https://demoqa.com/menu#')
    first = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(driver).move_to_element(first).click().perform()
    second = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(driver).move_to_element(second).click().perform()
    third = driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(driver).move_to_element(third).click().perform()


def test_3(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.find_element(By.ID, 'promptexample').click()
    Alert(driver).send_keys('Melsoft')
    Alert(driver).accept()
    message = driver.find_element(By.ID, 'promptreturn')
    assert "Melsoft" in message.text
