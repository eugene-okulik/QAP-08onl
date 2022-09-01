from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


service = Service(executable_path='chromedriver.exe')
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
