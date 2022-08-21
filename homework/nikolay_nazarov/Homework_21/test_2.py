import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        blank_text = self.driver.find_element(By.CLASS_NAME, "_blank").text
        assert blank_text == "Ecommerce software by PrestaShop™", \
            "В самом низу главной страницы нет текста " \
            "Ecommerce software by PrestaShop™"

    @pytest.mark.usefixtures('driver')
    def test_logo_is_visible(self):
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на главной странице"
        self.driver.find_element(By.CSS_SELECTOR, "[title = 'Women']").click()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице 'Women'"
        self.driver.find_element(By.CSS_SELECTOR, "ul.sf-menu > li:nth-child(2) > a").click()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице 'Dresses'"
        self.driver.find_element(By.CSS_SELECTOR, "ul.sf-menu > li:nth-child(3) > a").click()
        logo = self.driver.find_element(By.CSS_SELECTOR, "[alt='My Store']")
        assert logo, "Нет лого на странице 'T-shirts'"

    @pytest.mark.usefixtures('driver')
    def test_invalid_email_error_is_visible(self):
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()
        self.driver.find_element\
            (By.CSS_SELECTOR, "[title = 'Log in to your customer account']").click()
        email_input = self.driver.find_element(By.CSS_SELECTOR, "#email_create")
        email_input.send_keys("Мыло")
        email_input.send_keys(Keys.ENTER)
        error_text = self.driver.find_element(By.CSS_SELECTOR, ".alert-danger > ol > li").text
        assert error_text == "Invalid email address.", "Нет текста 'Invalid email address'"

    @pytest.mark.usefixtures('driver')
    def test_alphabetical_sorting_and_quality_control(self):
        self.driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
        self.driver.maximize_window()
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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button_start))
        button_start.click()
        button_one = self.driver.find_element(By.ID, 'button01')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button_one))
        button_one.click()
        button_two = self.driver.find_element(By.ID, 'button02')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button_two))
        button_two.click()
        button_three = self.driver.find_element(By.ID, 'button03')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button_three))
        button_three.click()
        button_check = self.driver.find_element(By.ID, 'buttonmessage')
        assert 'All Buttons Clicked' in button_check.text
