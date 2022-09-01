from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_blank_text(driver_chrome):
    driver_chrome.get("http://automationpractice.com/")
    driver_chrome.maximize_window()
    blank_text = driver_chrome.find_element(By.CLASS_NAME, "_blank").text
    assert blank_text == "Ecommerce software by PrestaShop™", \
        "В самом низу главной страницы нет текста " \
        "Ecommerce software by PrestaShop™"


def test_logo_is_visible(driver_chrome):
    driver_chrome.get("http://automationpractice.com/")
    driver_chrome.maximize_window()
    logo = driver_chrome.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на главной странице"
    driver_chrome.find_element(By.CSS_SELECTOR, "[title = 'Women']").click()
    logo = driver_chrome.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на странице 'Women'"
    driver_chrome.find_element(By.CSS_SELECTOR, "ul.sf-menu > li:nth-child(2) > a").click()
    logo = driver_chrome.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на странице 'Dresses'"
    driver_chrome.find_element(By.CSS_SELECTOR, "ul.sf-menu > li:nth-child(3) > a").click()
    logo = driver_chrome.find_element(By.CSS_SELECTOR, "[alt='My Store']")
    assert logo, "Нет лого на странице 'T-shirts'"


def test_invalid_email_error_is_visible(driver_chrome):
    driver_chrome.get("http://automationpractice.com/")
    driver_chrome.maximize_window()
    driver_chrome.find_element \
        (By.CSS_SELECTOR, "[title = 'Log in to your customer account']").click()
    email_input = driver_chrome.find_element(By.CSS_SELECTOR, "#email_create")
    email_input.send_keys("Мыло")
    email_input.send_keys(Keys.ENTER)
    error_text = driver_chrome.find_element(By.CSS_SELECTOR, ".alert-danger > ol > li").text
    assert error_text == "Invalid email address.", "Нет текста 'Invalid email address'"


def test_alphabetical_sorting_and_quality_control(driver_chrome):
    driver_chrome.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    driver_chrome.maximize_window()
    quantity = driver_chrome.find_element(By.CLASS_NAME, 'product-count')
    sort = Select(driver_chrome.find_element(By.ID, 'selectProductSort'))
    sort.select_by_value('name:asc')
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
    start_button = driver_chrome.find_element(By.ID, 'button00')
    start_button.click()
    first_button = driver_chrome.find_element(By.ID, 'button01')
    first_button.click()
    second_button = driver_chrome.find_element(By.ID, 'button02')
    second_button.click()
    third_button = driver_chrome.find_element(By.ID, 'button03')
    third_button.click()
    check_button = driver_chrome.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in check_button.text


def test_button_click_task_2(driver_chrome):
    driver_chrome.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    start_button = driver_chrome.find_element(By.ID, 'button00')
    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable(start_button))
    start_button.click()
    first_button = driver_chrome.find_element(By.ID, 'button01')
    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable(first_button))
    first_button.click()
    second_button = driver_chrome.find_element(By.ID, 'button02')
    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable(second_button))
    second_button.click()
    third_button = driver_chrome.find_element(By.ID, 'button03')
    WebDriverWait(driver_chrome, 10).until(EC.element_to_be_clickable(third_button))
    third_button.click()
    check_button = driver_chrome.find_element(By.ID, 'buttonmessage')
    assert 'All Buttons Clicked' in check_button.text
