from homework.Anastacia_Kuznetcova.homework23.pom.pages.log_in import AuthPage


def test_fill_inputs(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.mail_field()
    auth_page.mail_inp()
    auth_page.order_inp()
    auth_page.message_inp()
    auth_page.submit_btn()
    auth_page.alert()
    assert auth_page.alert() == 'There is 1 error\nPlease select a subject from the list provided.'


def test_search_product(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.search_form()
    auth_page.search_input()
    auth_page.search_btn()
    auth_page.search_res_txt()
    assert auth_page.search_res_txt() == '7 results have been found.'


def test_cart_check_txt(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.cart_check()
    auth_page.cart_alert_check()
    assert auth_page.cart_alert_check() == 'Your shopping cart is empty.'
