from selenium.webdriver.common.by import By

all_element = (By.XPATH, '//div[@id="ajax-filter-container"]/div[3]')
no_product = (By.XPATH, '//div[@id="ajax-filter-container"]/p')
power_supplies = (By.XPATH, '//*[@id="ajax-filter-container"]/div[3]/div[4]/div')
add_to_cat = (By.CSS_SELECTOR, '''button[onclick="cart.add('8534');"]''')
cat_link = (By.XPATH, '//*[@id="pc_header"]/div/div/div[3]/div[3]/a')
laptops_in_page = (By.XPATH, '//div[@id="ajax-filter-container"]/div[3]')
