import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class TestTask:

    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    @pytest.mark.usefixtures('driver')
    def test_copyright_info(self):
        self.driver.get('http://automationpractice.com/')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        copyright1 = self.driver.find_element(By.XPATH,
                                              '//section[@class="bottom-footer col-xs-12"]')
        assert "© 2014 Ecommerce software by PrestaShop™" in copyright1.text

    @pytest.mark.usefixtures('driver')
    def test_check_logo_on_page_women(self):
        self.driver.get('http://automationpractice.com')
        page_women = self.driver.find_element(By.XPATH, '//a[@title="Women"]')
        page_women.click()
        logo = self.driver.find_element(By.XPATH,
                                        '//img[@src="http://automationpractice.com/img/logo.jpg"]')
        assert logo

    @pytest.mark.usefixtures('driver')
    def test_check_logo_on_page_dresses(self):
        self.driver.get('http://automationpractice.com')
        page_dresses = self.driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a')
        page_dresses.click()
        logo = self.driver.find_element(By.XPATH,
                                        '//img[@src="http://automationpractice.com/img/logo.jpg"]')
        assert logo

    @pytest.mark.usefixtures('driver')
    def test_check_logo_on_page_t_shirts(self):
        self.driver.get('http://automationpractice.com')
        page_dresses = self.driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[3]/a')
        page_dresses.click()
        logo = self.driver.find_element(By.XPATH,
                                        '//img[@src="http://automationpractice.com/img/logo.jpg"]')
        assert logo

    @pytest.mark.usefixtures('driver')
    def test_invalid_email_address(self):
        self.driver.get('http://automationpractice.com/')
        sing_in = self.driver.find_element(By.XPATH, '//a[@class="login"]')
        sing_in.click()
        email_address = self.driver.find_element(By.ID, 'email_create')
        email_address.send_keys('мыло')
        button = self.driver.find_element(By.ID, 'SubmitCreate')
        button.click()
        alert_danger = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        alert_danger_text = alert_danger.find_element(By.TAG_NAME, 'li')
        assert "Invalid email address." in alert_danger_text.text

    @pytest.mark.usefixtures('driver')
    def test_alphabetical_sorting_and_quality_control(self):
        self.driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
        quantity = self.driver.find_element(By.CLASS_NAME, 'product-count')
        sort_alphabetically = Select(self.driver.find_element(By.ID, 'selectProductSort'))
        sort_alphabetically.select_by_value('name:asc')
        quantity_after_sort = self.driver.find_element(By.CLASS_NAME, 'product-count')
        assert quantity_after_sort.text == quantity.text

    @pytest.mark.usefixtures('driver')
    def test_add_to_cart(self):
        self.driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
        search_product = self.driver.find_element(By.LINK_TEXT, 'Printed Dress')
        actions = ActionChains(self.driver)
        actions.move_to_element(search_product)
        actions.perform()
        add_product_1 = self.driver.find_element(By.XPATH, '//a[@data-id-product="3"]')
        add_product_1.click()
        close_window = self.driver.find_element(By.XPATH, '//span[@class="cross"]')
        close_window.click()
        cart_after_add = self.driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
        assert 'Cart 1 Product' in cart_after_add.text

    @pytest.mark.usefixtures('driver')
    def test_button_click(self):
        self.driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
        button_start = self.driver.find_element(By.ID, 'button00')
        button_start.click()
        button_one = self.driver.find_element(By.ID, 'button01')
        button_one.click()
        button_two = self.driver.find_element(By.ID, 'button02')
        button_two.click()
        button_three = self.driver.find_element(By.ID, 'button03')
        button_three.click()
        button_check = self.driver.find_element(By.ID, 'buttonmessage')
        assert 'All Buttons Clicked' in button_check.text

    @pytest.mark.usefixtures('driver')
    def test_button_click_task_2(self):
        self.driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')
        button_start = self.driver.find_element(By.ID, 'button00')
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(button_start))
        button_start.click()
        button_one = self.driver.find_element(By.ID, 'button01')
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(button_one))
        button_one.click()
        button_two = self.driver.find_element(By.ID, 'button02')
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(button_two))
        button_two.click()
        button_three = self.driver.find_element(By.ID, 'button03')
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(button_three))
        button_three.click()
        button_check = self.driver.find_element(By.ID, 'buttonmessage')
        assert 'All Buttons Clicked' in button_check.text
