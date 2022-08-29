from homework.Anastacia_Kuznetcova.homework23.pom.pages.buttons import BtnPage


def test_btn_start_is_clickable(driver):
    btn_page = BtnPage(driver)
    btn_page.open()
    btn_page.btn_st()
    assert btn_page.btn_start_clickable()


def test_check_text(driver):
    btn_page = BtnPage(driver)
    btn_page.open()
    btn_page.its_text()
    assert btn_page.txt_is_displayed()


def test_btns(driver):
    btn_page = BtnPage(driver)
    btn_page.open()
    btn_page.btn_st()
    btn_page.its_btn_1()
    btn_page.its_btn_2()
    btn_page.its_btn_3()
    btn_page.its_btn_check()
    assert 'All Buttons Clicked' in btn_page.its_btn_check()
