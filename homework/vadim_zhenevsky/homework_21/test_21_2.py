import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select

serv = Service(executable_path='chromedriver.exe')
chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()


@pytest.fixture(scope='session')
def start_now():
    print("START")
    chrome_driver.get("http://automationpractice.com/")
    yield chrome_driver
    print("END")
    chrome_driver.quit()


def test_inscription_in_the_footer(start_now):
    footer_text = chrome_driver.find_element(By.CSS_SELECTOR,
                                             "section.bottom-footer.col-xs-12")
    assert footer_text.text == "© 2014 Ecommerce software by PrestaShop™"


def test_check_logo_on_page_woman(start_now):
    page_women = chrome_driver.find_element(By.XPATH, '//a[@title="Women"]')
    page_women.click()
    logo = chrome_driver.find_element(By.XPATH,
                                      '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_check_logo_on_page_dress(start_now):
    page_dresses = chrome_driver.find_element(By.XPATH,
                                              '//div[@id="block_top_menu"]/ul/li[2]/a')
    page_dresses.click()
    logo = chrome_driver.find_element(By.XPATH,
                                      '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_check_logo_on_page_t_shirts(start_now):
    page_t_shirts = chrome_driver.find_element(By.XPATH,
                                               '//div[@id="block_top_menu"]/ul/li[3]/a')
    page_t_shirts.click()
    logo = chrome_driver.find_element(By.XPATH,
                                      '//img[@src="http://automationpractice.com/img/logo.jpg"]')
    assert logo


def test_check_for_a_warning_message(start_now):
    chrome_driver.find_element(By.ID, 'contact-link').click()
    email = chrome_driver.find_element(By.CSS_SELECTOR,
                                       'input[data-validate="isEmail"]')
    email.click()
    email.send_keys('мыло')
    submit = chrome_driver.find_element(By.NAME, "submitMessage")
    submit.click()
    alert = chrome_driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    li_alert = alert.find_element(By.TAG_NAME, 'li')
    assert li_alert.text == 'Invalid email address.'


def test_check_sorting_and_quantity_of_goods_before_and_after_sorting(start_now):
    chrome_driver.find_element(By.XPATH, "//a[@title='Women']").click()
    quantity = chrome_driver.find_element(By.CLASS_NAME, "product-count").text
    sorting = Select(chrome_driver.find_element(By.ID, "selectProductSort"))
    sorting.select_by_index(3)
    quantity_after_sort = chrome_driver.find_element(By.CLASS_NAME, "product-count").text
    assert quantity == quantity_after_sort


def test_checking_the_addition_to_the_cart_and_display_in_it(start_now):
    search_product = chrome_driver.find_element(By.LINK_TEXT, 'Blouse')
    actions = ActionChains(chrome_driver)
    actions.move_to_element(search_product)
    actions.perform()
    add_product = chrome_driver.find_element(By.XPATH, '//a[@data-id-product="2"]')
    add_product.click()
    sleep(3)
    close_window = chrome_driver.find_element(By.XPATH, '//span[@class="cross"]')
    close_window.click()
    cart_after_add = chrome_driver.find_element(By.XPATH,
                                                '//a[@title="View my shopping cart"]')
    assert 'Cart 1 Product' in cart_after_add.text
