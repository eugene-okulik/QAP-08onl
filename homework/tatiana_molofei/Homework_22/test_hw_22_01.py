from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_goods_in_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')
    goods_button = driver.find_elements(By.CLASS_NAME, 'hrefch')
    goods_button[4].send_keys(Keys.LEFT_CONTROL, Keys.ENTER)
    new_window = driver.window_handles
    driver.switch_to.window(new_window[1])
    driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(new_window[0])
    driver.find_element(By.ID, 'cartur').click()
    goods_in_cart = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert 'Iphone 6 32gb' in goods_in_cart.text
