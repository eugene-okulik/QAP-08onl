# Первый тест
# https://www.demoblaze.com/index.html
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test1(driver_chrome):
    driver_chrome.get("https://www.demoblaze.com/index.html")
    driver_chrome.maximize_window()
    sleep(3)
    new_tab = driver_chrome.find_elements(By.CLASS_NAME, 'hrefch')
    new_tab[6].send_keys(Keys.LEFT_CONTROL, Keys.ENTER)
    sleep(3)
    windows = driver_chrome.window_handles
    driver_chrome.switch_to.window(windows[1])
    driver_chrome.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(7)"]').click()
    sleep(3)
    WebDriverWait(driver_chrome, 10).until(EC.alert_is_present())
    Alert(driver_chrome).accept()
    driver_chrome.close()
    driver_chrome.switch_to.window(windows[0])
    driver_chrome.find_element(By.ID, "cartur").click()
    basket = driver_chrome.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert "HTC One M9" in basket.text
    sleep(5)
