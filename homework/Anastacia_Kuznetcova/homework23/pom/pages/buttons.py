from homework.Anastacia_Kuznetcova.homework23.pom.pages.base_page import BasePage
from homework.Anastacia_Kuznetcova.homework23.pom.pages.locators import buttons_locators as bl


class BtnPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html')

    def btn_st(self):
        return self.find_element(bl.btn_start).click()

    def its_btn_1(self):
        return self.find_element(bl.btn_1).click()

    def its_text(self):
        return self.find_element(bl.text).text

    def its_btn_2(self):
        return self.find_element(bl.btn_2).click()

    def its_btn_3(self):
        return self.find_element(bl.btn_3).click()

    def its_btn_check(self):
        return self.find_element(bl.btn_check).text

    def btn_start_clickable(self):
        return self.find_element(bl.btn_start).is_enabled()

    def txt_is_displayed(self):
        return self.find_element(bl.text).is_displayed()
