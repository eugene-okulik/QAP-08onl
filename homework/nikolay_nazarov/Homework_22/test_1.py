from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test_blank_text(chrome_driver):
    chrome_driver.get("https://www.demoblaze.com/index.html")
    chrome_driver.maximize_window()
    samsung_galaxy_item = chrome_driver.find_element(By.CLASS_NAME, "h-100")
    ActionChains(chrome_driver).move_to_element(samsung_galaxy_item).key_down(Keys.CONTROL). \
        click().key_up(Keys.CONTROL).perform()
    chrome_driver.switch_to.window(chrome_driver.window_handles[1])
    item_name_to_add = chrome_driver.find_element(By.CSS_SELECTOR, ".name:nth-child(1)").text
    add_to_card_button = chrome_driver.find_element(By.CLASS_NAME, "btn-success")
    add_to_card_button.click()
    WebDriverWait(chrome_driver, 10).until(EC.alert_is_present())
    chrome_driver.switch_to.alert.accept()
    chrome_driver.close()
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    chrome_driver.find_element(By.ID, "cartur").click()
    item_in_cart_text = chrome_driver.find_element(By.CSS_SELECTOR,
                                                   ".success > td:nth-child(2)").text
    assert item_name_to_add == item_in_cart_text, f"{item_name_to_add} " \
                                                  f"не равен {item_in_cart_text}"


def test_task_move(chrome_driver):
    chrome_driver.get('https://demoqa.com/menu# ')
    main_items_2 = chrome_driver.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(chrome_driver).move_to_element(main_items_2).perform()
    sub_list = chrome_driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(chrome_driver).move_to_element(sub_list).perform()
    sub_items_2 = chrome_driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(chrome_driver).move_to_element(sub_items_2).perform()


def test_check_alert(chrome_driver):
    chrome_driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    chrome_driver.find_element(By.ID, 'promptexample').click()
    Alert(chrome_driver).send_keys('QAP-08onl')
    Alert(chrome_driver).accept()
    check_text = chrome_driver.find_element(By.ID, 'promptreturn')
    assert check_text.text == 'QAP-08onl'
