# https://www.demoblaze.com/index.html
#
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли

"""module"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test1(chrome_driver):
    """module"""
    chrome_driver.get("https://www.demoblaze.com/index.html")
    chrome_driver.maximize_window()
    sleep(3)
    my_tab = chrome_driver.find_elements(By.CLASS_NAME, 'hrefch')
    my_tab[0].send_keys(Keys.LEFT_CONTROL, Keys.ENTER)
    sleep(3)
    windows = chrome_driver.window_handles
    chrome_driver.switch_to.window(windows[1])
    chrome_driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]').click()
    sleep(3)
    WebDriverWait(chrome_driver, 10).until(EC.alert_is_present())
    Alert(chrome_driver).accept()
    chrome_driver.close()
    chrome_driver.switch_to.window(windows[0])
    chrome_driver.find_element(By.ID, "cartur").click()
    basket = chrome_driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert "Samsung galaxy s6" in basket.text
    sleep(5)
