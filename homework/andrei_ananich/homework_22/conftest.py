import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def chrome_driver():
    service = Service(executable_path="C:\\Users\\Lenovo\\QAP-08onl\\homework\\"
                                      "andrei_ananich\\selenium\\chromedriver.exe")
    chrome_driver = webdriver.Chrome(service=service)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()
