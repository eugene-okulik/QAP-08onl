import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class TestTask:

    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    @pytest.mark.usefixtures('driver')
    def test_blank_text(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        samsung_galaxy_item = self.driver.find_element(By.CLASS_NAME, "h-100")
        ActionChains(self.driver).move_to_element(samsung_galaxy_item).key_down(Keys.CONTROL).\
            click().key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[1])
        item_name_to_add = self.driver.find_element(By.CSS_SELECTOR, ".name:nth-child(1)").text
        add_to_card_button = self.driver.find_element(By.CLASS_NAME, "btn-success")
        add_to_card_button.click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element(By.ID, "cartur").click()
        item_in_cart_text = self.driver.find_element(By.CSS_SELECTOR,
                                                     ".success > td:nth-child(2)").text
        assert item_name_to_add == item_in_cart_text, f"{item_name_to_add} " \
                                                      f"не равен {item_in_cart_text}"

    @pytest.mark.usefixtures('driver')
    def test_task_move(self):
        self.driver.get('https://demoqa.com/menu# ')
        main_items_2 = self.driver.find_element(By.LINK_TEXT, 'Main Item 2')
        ActionChains(self.driver).move_to_element(main_items_2).perform()
        sub_list = self.driver.find_element(By.LINK_TEXT, 'SUB SUB LIST »')
        ActionChains(self.driver).move_to_element(sub_list).perform()
        sub_items_2 = self.driver.find_element(By.LINK_TEXT, 'Sub Sub Item 2')
        ActionChains(self.driver).move_to_element(sub_items_2).perform()

    @pytest.mark.usefixtures('driver')
    def test_check_alert(self):
        self.driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
        self.driver.find_element(By.ID, 'promptexample').click()
        Alert(self.driver).send_keys('QAP-08onl')
        Alert(self.driver).accept()
        check_text = self.driver.find_element(By.ID, 'promptreturn')
        assert check_text.text == 'QAP-08onl'
