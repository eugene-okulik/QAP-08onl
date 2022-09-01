from pages.about_us_page import AboutPage


def test_t_shirt_is_displayed(driver):
    about_us_page = AboutPage(driver)
    about_us_page.open()
    assert about_us_page.t_shirts_is_displayed()


def test_dresses_is_displayed(driver):
    about_us_page = AboutPage(driver)
    about_us_page.open()
    assert about_us_page.dresses_is_displayed()


def test_logo_is_displayed(driver):
    about_us_page = AboutPage(driver)
    about_us_page.open()
    assert about_us_page.logo_is_displayed()
