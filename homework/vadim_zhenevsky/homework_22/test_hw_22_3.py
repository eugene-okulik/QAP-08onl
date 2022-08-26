from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_three(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    show_prompt_box_button = driver.find_element(By.ID, 'promptexample')
    show_prompt_box_button.click()
    Alert(driver).send_keys('HOMEWORK22')
    Alert(driver).accept()
    check_text = driver.find_element(By.ID, 'promptreturn')
    print(check_text.text)
    assert check_text.text == 'HOMEWORK22'
