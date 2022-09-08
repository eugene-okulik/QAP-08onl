from ..pages.journal_page import JournalPage


def test_journal(driver):
    journal_page = JournalPage(driver)
    journal_page.open()
    journal_page.open_journal()
    assert journal_page.test_subscription_button_is_displayed()
