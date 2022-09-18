from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_alert_text(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    promt_box_button = driver.find_element(By.ID, 'promptexample')
    promt_box_button.click()
    Alert(driver).send_keys('This test will be passed')
    Alert(driver).accept()
    assert 'This test will be passed' in driver.find_element(By.ID, 'promptreturn').text
