from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def test_copyright_info(driver_chrome):
    driver_chrome.get('http://automationpractice.com/')
    driver_chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    copyright1 = driver_chrome.find_element(
        By.XPATH, '//section[@class="bottom-footer col-xs-12"]'
    )
    assert "© 2014 Ecommerce software by PrestaShop™" in copyright1.text


def test_check_logo_on_page_women(driver_chrome):
    driver_chrome.get('http://automationpractice.com')
    page_women = driver_chrome.find_element(By.XPATH, '//a[@title="Women"]')
    page_women.click()
    logo = driver_chrome.find_element(
        By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]'
    )
    assert logo


def test_check_logo_on_page_dresses(driver_chrome):
    driver_chrome.get('http://automationpractice.com')
    page_dresses = driver_chrome.find_element(
        By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a'
    )
    page_dresses.click()
    logo = driver_chrome.find_element(
        By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]'
    )
    assert logo


def test_check_logo_on_page_t_shirts(driver_chrome):
    driver_chrome.get('http://automationpractice.com')
    page_dresses = driver_chrome.find_element(
        By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a'
    )
    page_dresses.click()
    logo = driver_chrome.find_element(
        By.XPATH, '//img[@src="http://automationpractice.com/img/logo.jpg"]'
    )
    assert logo


def test_invalid_email_address(driver_chrome):
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


def test_alphabetical_sorting_and_quality_control(driver_chrome):
    driver_chrome.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    quantity = driver_chrome.find_element(By.CLASS_NAME, 'product-count')
    sort_alphabetically = Select(driver_chrome.find_element(By.ID, 'selectProductSort'))
    sort_alphabetically.select_by_value('name:asc')
    quantity_after_sort = driver_chrome.find_element(By.CLASS_NAME, 'product-count')
    assert quantity_after_sort.text == quantity.text


def test_add_to_cart(driver_chrome):
    driver_chrome.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    search_product = driver_chrome.find_element(By.LINK_TEXT, 'Printed Dress')
    actions = ActionChains(driver_chrome)
    actions.move_to_element(search_product)
    actions.perform()
    add_product_1 = driver_chrome.find_element(By.XPATH, '//a[@data-id-product="3"]')
    add_product_1.click()
    close_window = driver_chrome.find_element(By.XPATH, '//span[@class="cross"]')
    close_window.click()
    cart_after_add = driver_chrome.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert 'Cart 1 Product' in cart_after_add.text


def test_button_click(driver_chrome):
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
    button_start = driver_chrome.find_element(By.ID, 'button00')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(button_start))
    button_start.click()
    button_one = driver_chrome.find_element(By.ID, 'button01')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(button_one))
    button_one.click()
    button_two = driver_chrome.find_element(By.ID, 'button02')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(button_two))
    button_two.click()
    button_three = driver_chrome.find_element(By.ID, 'button03')
    WebDriverWait(driver_chrome, 10).until(ec.element_to_be_clickable(button_three))
    button_three.click()
    button_check = driver_chrome.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in button_check.text
