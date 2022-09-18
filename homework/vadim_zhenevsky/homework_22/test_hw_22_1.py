from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    samsung_galaxy_s6 = driver.find_element(By.CSS_SELECTOR,
                                            'a[href="prod.html?idp_=1"]')
    ActionChains(driver).move_to_element(samsung_galaxy_s6).key_down(Keys.CONTROL). \
        click(samsung_galaxy_s6).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    add_to_cart = driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')
    add_to_cart.click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart_open = driver.find_element(By.ID, "cartur")
    cart_open.click()
    cart_check = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    print(cart_check.text)
    assert cart_check.text == 'Samsung galaxy s6'
