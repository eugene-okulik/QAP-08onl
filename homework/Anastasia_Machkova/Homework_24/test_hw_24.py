from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys
import allure


@allure.feature('Homework_24')
@allure.story('iPhone exists in the cart')
def test_1(driver):
    with allure.step('Open site'):
        driver.get('https://www.demoblaze.com/index.html')
    with allure.step('Move to a new tab'):
        new_tab = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=5"]')
        ActionChains(driver).move_to_element(new_tab).key_down(Keys.CONTROL).click(new_tab).\
            key_up(Keys.CONTROL).perform()
        driver.switch_to.window(driver.window_handles[1])
    with allure.step('Add to cart'):
        driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(5)"]').click()
    with allure.step('Alert is present'):
        WebDriverWait(driver, 10).until(ec.alert_is_present())
        Alert(driver).accept()
        driver.close()
    with allure.step('Go to cart'):
        driver.switch_to.window(driver.window_handles[0])
        cart = driver.find_element(By.ID, 'cartur')
        ActionChains(driver).move_to_element(cart).click().perform()
    with allure.step('Check if iPhone in the cart'):
        iphone = driver.find_element(By.XPATH, '//tbody[@id="tbodyid"]/tr/td[2]')
    assert "Iphone 6 32gb" in iphone.text


@allure.feature('Homework_24')
@allure.story('Click all buttons')
def test_2(driver):
    with allure.step('Open site'):
        driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html')
    with allure.step('Find all buttons'):
        driver.find_element(By.ID, 'button00').click()
        button_1 = driver.find_element(By.ID, 'button01')
        button_2 = driver.find_element(By.ID, 'button02')
        button_3 = driver.find_element(By.ID, 'button03')
    with allure.step('Wait and click all button'):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_1))
        button_1.click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_2))
        button_2.click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(button_3))
        button_3.click()
        all_buttons_clicked = driver.find_element(By.ID, 'buttonmessage')
    assert all_buttons_clicked.text == 'All Buttons Clicked'


@allure.feature('Homework_24')
@allure.story('Melsoft in the field')
def test_3(driver):
    with allure.step('Open site'):
        driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    with allure.step('Accept alert'):
        driver.find_element(By.ID, 'promptexample').click()
        Alert(driver).send_keys('Melsoft')
        Alert(driver).accept()
        message = driver.find_element(By.ID, 'promptreturn')
    assert "Melsoft" in message.text
