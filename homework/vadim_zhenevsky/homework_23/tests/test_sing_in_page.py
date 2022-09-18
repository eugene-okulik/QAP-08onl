from time import sleep
from homework_23.pages.home_page import HomePage
from selenium.webdriver.common.by import By


def test_open_login_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sing_in()
    check_login_page = driver.find_element(By.CLASS_NAME,
                                           'socials-auth__title')
    print(check_login_page.text)
    assert check_login_page.text == 'Вход через соц. сети:'


def test_fill_out_the_login_form_with_a_password_error(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sing_in()
    email_field = driver.find_element(By.ID, 'login-profile.email')
    email_field.send_keys('testzaovadim@gmail.com')
    password_field = driver.find_element(By.ID, 'login-profile.password')
    password_field.send_keys('123456789')
    click_enter_button = driver.find_element(By.CLASS_NAME, 'button_submit')
    click_enter_button.click()
    sleep(3)
    check_error_message = driver.find_element(By.CLASS_NAME, 'modal__text')
    print(check_error_message.text)
    assert check_error_message.text == 'Пожалуйста, введите корректные имя ' \
                                       'пользователя и пароль. Оба поля могут ' \
                                       'быть чувствительны к регистру.'


def test_password_recovery(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_sing_in()
    forgot_password_button = driver.find_element(By.CLASS_NAME,
                                                 'form__link-btn_remind')
    forgot_password_button.click()
    check_forgot_password_page = driver.find_element(By.CLASS_NAME, 'title')
    print(check_forgot_password_page.text)
    email_field = driver.find_element(By.ID, 'login-profile')
    email_field.send_keys('testzaovadim@gmail.com')
    send_password_button = driver.find_element(By.CLASS_NAME, 'button_submit')
    send_password_button.click()
    check_message = driver.find_element(By.CLASS_NAME, 'modal__title')
    print(check_message.text)
    assert check_message.text == 'Готово!'
