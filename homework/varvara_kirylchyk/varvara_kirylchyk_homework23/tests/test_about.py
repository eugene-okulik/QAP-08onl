from ..pages.about import AboutPage

def test_big_map(driver):
    page =AboutPage(driver)
    page.open()
    assert page.company_field().is_displayed()


def test_logo(driver):
    page = AboutPage(driver)
    page.open()
    assert page.team_field().is_displayed()


def test_address(driver):
    page = AboutPage(driver)
    page.open()
    assert page.testimonials_field().is_displayed()
