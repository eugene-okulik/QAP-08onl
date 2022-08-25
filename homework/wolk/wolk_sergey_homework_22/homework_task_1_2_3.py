from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service = Service(executable_path='chromedriver.exe')
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.maximize_window()


def test_availability():
    driver.get('https://www.demoblaze.com/index.html')
    lot = driver.find_element(By.CSS_SELECTOR, 'a[href="prod.html?idp_=9"]')
    ActionChains(driver).move_to_element(lot).key_down(Keys.CONTROL).\
        click(lot).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    choose_a_lott = driver.find_element(By.CSS_SELECTOR, 'h2[class="name"]').text
    driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(9)"]').click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    card = driver.find_element(By.ID, "cartur")
    ActionChains(driver).move_to_element(card).click().perform()
    lot_model = driver.find_element(By.XPATH, '//tbody[@id="tbodyid"]/tr/td[2]')
    assert lot_model.text == choose_a_lott


def test_move():
    driver.get('https://demoqa.com/menu# ')
    main = driver.find_element(By.LINK_TEXT, 'Main Item 2')
    ActionChains(driver).move_to_element(main).perform()
    list_5 = driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
    ActionChains(driver).move_to_element(list_5).perform()
    sub_it = driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
    ActionChains(driver).move_to_element(sub_it).perform()


def test_alert():
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.find_element(By.ID, 'promptexample').click()
    Alert(driver).send_keys('Love_Python!')
    Alert(driver).accept()
    text = driver.find_element(By.ID, 'promptreturn')
    assert text.text == 'Love_Python!'
