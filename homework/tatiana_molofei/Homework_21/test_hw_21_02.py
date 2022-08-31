from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


def _open_driver(driver):
    driver.get('http://automationpractice.com/index.php')
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Test 1
# Проверить, что в самом низу главной страницы есть текст “© 2014 Ecommerce software by PrestaShop™”


# @pytest.mark.usefixtures('_open_driver')
def test_text_at_end_page(driver):
    driver.get('http://automationpractice.com/index.php')
    text_at_end_page = driver.find_element(By.XPATH, '//section[@class="bottom-footer col-xs-12"]')
    assert text_at_end_page.text == "© 2014 Ecommerce software by PrestaShop™"

# Test 2
# Проверить, что логотип отображается во всех трех категориях сайта (woman, dresses, t-shirts)


def test_titles_are_displayed(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//a[@title="Women"]').click()
    assert driver.find_element(By.ID, 'header_logo').is_displayed()
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a').click()
    assert driver.find_element(By.ID, 'header_logo').is_displayed()
    driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a').click()
    assert driver.find_element(By.ID, 'header_logo').is_displayed()

# Test 3
# Проверить, что сообщение “Invalid email address.” появляется
# если ввести слово “мыло” в поле емейл и попытаться создать аккаун


def test_email_address(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.CLASS_NAME, "login").click()
    email_address = driver.find_element(By.ID, 'email_create')
    email_address.send_keys("мыло")
    create_email_button = driver.find_element(By.ID, 'SubmitCreate')
    create_email_button.submit()
    alert_header = driver.find_element(By.CLASS_NAME, 'alert-danger')
    alert_header_text = alert_header.find_element(By.TAG_NAME, 'li')
    assert alert_header_text.text == "Invalid email address."

# Test 4
# На сайте на странице women отсортировать товары по алфавиту
# (над списком товаров на странице есть дропдаун "Sort by")
# После сортировки проверить, что товаров на странице столько же сколько было до сортировки.


def test_sort_goods(driver):
    driver.get('http://automationpractice.com/index.php')
    driver.find_element(By.XPATH, '//a[@title="Women"]').click()
    sort_by_button = driver.find_element(By.ID, 'selectProductSort')
    sort_by_button.click()
    select = Select(driver.find_element(By.ID, 'selectProductSort'))
    select.select_by_index(3)
    amount_goods = driver.find_element(By.CLASS_NAME, 'product-count')
    assert amount_goods.text == "Showing 1 - 7 of 7 items"

# Test 5
# На том же сайте добавить товар в корзину и проверить, что товар появился в корзине


def test_add_goods_in_basket(driver):
    driver.get('http://automationpractice.com/index.php')
    goods_button = driver.find_element(By.LINK_TEXT, 'Blouse')
    action = ActionChains(driver)
    action.move_to_element(goods_button)
    action.perform()
    add_goods = driver.find_element(By.XPATH, '//a[@data-id-product="2"]')
    add_goods.click()
    close_new_window = driver.find_element(By.XPATH, '//span[@class="cross"]')
    close_new_window.click()
    basket_text = driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
    assert basket_text.text != 'empty'

# Test 6
# Нужно кликнуть на все 4 кнопки (появляются последовательно)


def test_text_after_click_button1(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
    start_button = driver.find_element(By.ID, 'button00')
    start_button.click()
    second_button = driver.find_element(By.ID, 'button01')
    second_button.click()
    # driver.implicitly_wait(10)
    third_button = driver.find_element(By.ID, 'button02')
    third_button.click()
    # driver.implicitly_wait(10)
    forth_button = driver.find_element(By.ID, 'button03')
    forth_button.click()
    # driver.implicitly_wait(10)
    text_after_click = driver.find_element(By.ID, 'buttonmessage')
    assert text_after_click.text == "All Buttons Clicked"

# Test 7
# Нужно кликнуть на все 4 кнопки (активируются последовательно)


def test_text_after_click_button2(driver):
    driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html')
    # driver.implicitly_wait(10)
    start_button = driver.find_element(By.ID, 'button00')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(start_button))
    start_button.click()
    second_button = driver.find_element(By.ID, 'button01')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(second_button))
    second_button.click()
    third_button = driver.find_element(By.ID, 'button02')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(third_button))
    third_button.click()
    forth_button = driver.find_element(By.ID, 'button03')
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable(forth_button))
    forth_button.click()
    text_after_click = driver.find_element(By.ID, 'buttonmessage')
    assert text_after_click.text == "All Buttons Clicked"
