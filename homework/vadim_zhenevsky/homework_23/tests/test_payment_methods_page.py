from homework_23.pages.home_page import HomePage
from selenium.webdriver.common.by import By


def test_open_payment_methods_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_payment_methods_page()
    check_payment_methods_page = driver.find_element(By.CLASS_NAME, 'billboard__title')
    print(check_payment_methods_page.text)
    assert check_payment_methods_page.text == 'Способы оплаты'
