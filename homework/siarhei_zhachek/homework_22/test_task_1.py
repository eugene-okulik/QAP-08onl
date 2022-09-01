from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_checking_the_availability_of_goods_in_the_cart(driver_chrome):
    driver_chrome.get('https://www.demoblaze.com/index.html')
    product = driver_chrome.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=9"]')
    ActionChains(driver_chrome).move_to_element(product).key_down(Keys.CONTROL).\
        click(product).key_up(Keys.CONTROL).perform()
    driver_chrome.switch_to.window(driver_chrome.window_handles[1])
    choose_a_product = driver_chrome.find_element(By.CSS_SELECTOR, 'h2[class="name"]').text
    driver_chrome.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(9)"]').click()
    WebDriverWait(driver_chrome, 10).until(ec.alert_is_present())
    Alert(driver_chrome).accept()
    driver_chrome.close()
    driver_chrome.switch_to.window(driver_chrome.window_handles[0])
    card = driver_chrome.find_element(By.ID, "cartur")
    ActionChains(driver_chrome).move_to_element(card).click().perform()
    product_model = driver_chrome.find_element(By.XPATH, '//tbody[@id="tbodyid"]/tr/td[2]')
    assert product_model.text == choose_a_product


def test_task_move(driver_chrome):
    driver_chrome.get('https://demoqa.com/menu# ')
    main_items_2 = driver_chrome.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(driver_chrome).move_to_element(main_items_2).perform()
    sub_list = driver_chrome.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(driver_chrome).move_to_element(sub_list).perform()
    sub_items_2 = driver_chrome.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(driver_chrome).move_to_element(sub_items_2).perform()


def test_check_alert(driver_chrome):
    driver_chrome.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver_chrome.find_element(By.ID, 'promptexample').click()
    Alert(driver_chrome).send_keys('Hello world!')
    Alert(driver_chrome).accept()
    check_text = driver_chrome.find_element(By.ID, 'promptreturn')
    assert check_text.text == 'Hello world!'
