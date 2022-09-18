from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def test_main_page_txt(driver_chrome):
    driver_chrome.get('http://automationpractice.com/')
    driver_chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    main_page_txt = driver_chrome.find_element(
        By.XPATH, '//section[@class="bottom-footer col-xs-12"]'
    )
    assert "© 2014 Ecommerce software by PrestaShop™" in main_page_txt.text


def test_check_logo(driver_chrome):
    res = 0
    driver_chrome.get('http://automationpractice.com')
    page_women = driver_chrome.find_element(By.XPATH, '//a[@title="Women"]')
    page_women.click()
    logo_women = driver_chrome.find_element(
        By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]'
    )
    if logo_women.is_displayed():
        res += 1

    driver_chrome.get('http://automationpractice.com')
    page_dresses = driver_chrome.find_element(
        By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a'
    )
    page_dresses.click()
    logo_dresses = driver_chrome.find_element(
        By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]'
    )
    if logo_dresses.is_displayed():
        res += 1

    driver_chrome.get('http://automationpractice.com')
    page_t_shirt = driver_chrome.find_element(
        By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a'
    )
    page_t_shirt.click()
    logo_t_shirt = driver_chrome.find_element(
        By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]'
    )
    if logo_t_shirt.is_displayed():
        res += 1
    assert res == 3


def test_invalid_email(driver_chrome):
    driver_chrome.get('http://automationpractice.com/')
    sing_in = driver_chrome.find_element(By.XPATH, '//a[@class="login"]')
    sing_in.click()
    email_address = driver_chrome.find_element(By.ID, 'email_create')
    email_address.send_keys('мыло')
    button = driver_chrome.find_element(By.ID, 'SubmitCreate')
    button.click()
    alert_danger = driver_chrome.find_element(By.CLASS_NAME, 'alert-danger')
    alert_danger_text = alert_danger.find_element(By.TAG_NAME, 'li')
    assert "Invalid email address." in alert_danger_text.text


def test_alphanumeric_sort_and_quantity_check(driver_chrome):
    driver_chrome.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    quantity = driver_chrome.find_element(By.CLASS_NAME, 'product-count')
    alphanumeric_sort = Select(driver_chrome.find_element(By.ID, 'selectProductSort'))
    alphanumeric_sort.select_by_value('name:asc')
    quantity_check = driver_chrome.find_element(By.CLASS_NAME, 'product-count')
    assert quantity_check.text == quantity.text


def test_add_to_cart(driver_chrome):
    driver_chrome.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    search_product = driver_chrome.find_element(By.LINK_TEXT, 'Printed Dress')
    actions = ActionChains(driver_chrome)
    actions.move_to_element(search_product)
    actions.perform()
    add_thing = driver_chrome.find_element(By.XPATH, '//a[@data-id-product="3"]')
    add_thing.click()
    close_window = driver_chrome.find_element(By.XPATH, '//span[@class="cross"]')
    close_window.click()
    cart_after_adding = driver_chrome.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert 'Cart 1 Product' in cart_after_adding.text


def test_button_click_task_1(driver_chrome):
    driver_chrome.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    button_start = driver_chrome.find_element(By.ID, 'button00')
    button_start.click()
    button_one = driver_chrome.find_element(By.ID, 'button01')
    button_one.click()
    button_two = driver_chrome.find_element(By.ID, 'button02')
    button_two.click()
    button_three = driver_chrome.find_element(By.ID, 'button03')
    button_three.click()
    button_check = driver_chrome.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in button_check.text


def test_button_click_task_2(driver_chrome):
    driver_chrome.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    btn_start = driver_chrome.find_element(By.ID, 'button00')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(btn_start))
    btn_start.click()
    btn_1 = driver_chrome.find_element(By.ID, 'button01')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(btn_1))
    btn_1.click()
    btn_2 = driver_chrome.find_element(By.ID, 'button02')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(btn_2))
    btn_2.click()
    btn_3 = driver_chrome.find_element(By.ID, 'button03')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(btn_3))
    btn_3.click()
    btn_check = driver_chrome.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in btn_check.text
