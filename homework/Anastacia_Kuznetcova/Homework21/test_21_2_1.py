from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture(scope='session')
def start_now():
    serv = Service(executable_path=r'D:\dz1\prog\chromedriver.exe')
    driver = webdriver.Chrome(service=serv)
    print("Начинаем")
    driver.get("http://automationpractice.com/")
    yield driver
    print("Заканчиваем")
    driver.quit()


# pylint: disable=redefined-outer-name
def test1(start_now):
    # pylint: disable=unused-argument, no-self-use
    bottom_text = driver.find_element(By.CSS_SELECTOR,
                                      "#footer > div > section.bottom-footer.col-xs-12 > div")
    assert bottom_text.text == "© 2014 Ecommerce software by PrestaShop™"


def test2():
    driver.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[1]/a").click()
    driver.implicitly_wait(5)
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test3():
    driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a').click()
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test4():
    driver.find_element(By.XPATH, "//*[@id=\"block_top_menu\"]/ul/li[3]/a").click()
    assert driver.find_element(By.CLASS_NAME, "logo").is_displayed()


def test_4():
    driver.find_element(By.ID, 'contact-link').click()
    email = driver.find_element(By.CSS_SELECTOR, 'input[data-validate="isEmail"]')
    email.click()
    email.send_keys('мыло')
    submit = driver.find_element(By.NAME, "submitMessage")
    submit.click()
    alert = driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]')
    li_header = alert.find_element(By.TAG_NAME, 'li')
    assert li_header.text == 'Invalid email address.'


def test_5():
    driver.find_element(By.XPATH, "//a[@title='Women']").click()
    text_starting = driver.find_element(By.CLASS_NAME, "product-count").text
    sort = Select(driver.find_element(By.ID, "selectProductSort"))
    sort.select_by_index(3)
    text_ending = driver.find_element(By.CLASS_NAME, "product-count").text
    assert text_starting == text_ending, "Error"


def test_6():
    driver.find_element(By.CLASS_NAME, "logo").click()
    driver.find_element(By.CSS_SELECTOR, "a[data-id-product='1']").click()
    assert driver.find_element(By.CLASS_NAME,
                               "ajax_cart_no_product").text != "empty"
