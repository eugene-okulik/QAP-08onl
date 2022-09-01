from selenium.webdriver.common.by import By

search_field = (By.XPATH, '//div[@id="search"]/input')
search_button = (By.XPATH, '//div[@id="search"]/span/button')
catalog = (By.XPATH, '//nav[@id="horizontal-menu"]/div[2]/ul/li[1]')
computers_and_accessories = (By.XPATH, '//*[@id="horizontal-menu"]/div[2]/ul/li[1]/div/ul/li[7]/a')
power_supplies = (By.XPATH, '//*[@id="horizontal-menu"]/div[2]/ul/li[1]/div/ul/li[7]/ul/li[2]/a')
cat_link = (By.XPATH, '//header[@id="pc_header"]/div/div/div[3]/div[3]/a')
laptops_und_computer = (By.XPATH, '//*[@id="horizontal-menu"]/div[2]/ul/li[1]/div/ul/li[10]/a')
notebooks = (By.XPATH, '//*[@id="horizontal-menu"]/div[2]/ul/li[1]/div/ul/li[10]/ul/li[3]/a')
