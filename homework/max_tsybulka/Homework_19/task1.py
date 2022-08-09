from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_test(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.set_window_size(2048, 1080)
        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        self.driver.find_element(By.ID, "id_contact").click()
        dropdown = self.driver.find_element(By.ID, "id_contact")
        dropdown.find_element(By.XPATH, "//option[. = 'Customer service']").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("maksim.pvo@gmail.com")
        self.driver.find_element(By.ID, "id_order").click()
        self.driver.find_element(By.ID, "id_order").send_keys("test")
        self.driver.find_element(By.ID, "message").click()
        self.driver.find_element(By.ID, "message").send_keys("this is my test message")
        self.driver.find_element(By.CSS_SELECTOR, "#submitMessage > span").click()
