from selenium.webdriver.common.by import By

element_to_cat = (By.XPATH, '//*[@id="content"]/div/div[2]/form')
element_is_not_to_cat = (By.XPATH, '//div[@id="content"]/p')
delete_product = (
    By.XPATH, '//*[@id="content"]/div/div[2]/form/div[2]/div/div[2]/div/div[3]/div/div[2]/button[2]'
)
