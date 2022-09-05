from selenium.webdriver.common.by import By
from ..pages.base_page_dev_by import BasePage


# pylint: too-few-public-methods
ANDERSEN_LABEL = (By.XPATH, '//div[@class="left"]/h1')


class AndersenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_label(self):
        return self.find_element(ANDERSEN_LABEL)
