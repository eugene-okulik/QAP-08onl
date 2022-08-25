"""System module."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def setup():
    """A dummy docstring."""
    print("Opening Browser")
    options = Options()
    options.add_argument('window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    print("Closing Browser")
    chrome_driver.quit()

# Задание 6
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html
# Нужно кликнуть на все 4 кнопки
# (появляются последовательно)
# В результате теста проверить,
# что текст “All Buttons Clicked” появился на экране
# Подсказка: здесь достаточно implicitly_wait

def test10(setup):
    """A dummy docstring."""
    setup.get("https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html")
    setup.find_element(By.ID, "button00").click()
    setup.implicitly_wait(5)
    assert setup.find_element(By.ID, "button01").is_displayed()
    setup.implicitly_wait(5)
    setup.find_element(By.ID, "button01").click()
    setup.implicitly_wait(5)
    assert setup.find_element(By.ID, "button02").is_displayed()
    setup.find_element(By.ID, "button02").click()
    setup.implicitly_wait(5)
    assert setup.find_element(By.ID, "button03").is_displayed()
    setup.implicitly_wait(5)
    setup.find_element(By.ID, "button03").click()
    assert setup.find_element(By.ID, "buttonmessage").text == \
        'All Buttons Clicked'

# Задание 7
# Тест для этой страницы -
# https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html
# Нужно кликнуть на все 4 кнопки (активируются последовательно)
# В результате теста проверить,
# что текст “All Buttons Clicked” появился на экране


def test11(setup):
    """A dummy docstring."""
    setup.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
    setup.find_element(By.ID, 'button00').click()
    setup.implicitly_wait(5)
    one = setup.find_element(By.ID, 'button01')
    two = setup.find_element(By.ID, 'button02')
    three = setup.find_element(By.ID, 'button03')
    WebDriverWait(setup, 10).until(EC.element_to_be_clickable(one))
    one.click()
    WebDriverWait(setup, 10).until(EC.element_to_be_clickable(two))
    two.click()
    WebDriverWait(setup, 10).until(EC.element_to_be_clickable(three))
    three.click()
    assert setup.find_element(By.ID, "buttonmessage").text == \
       'All Buttons Clicked'
