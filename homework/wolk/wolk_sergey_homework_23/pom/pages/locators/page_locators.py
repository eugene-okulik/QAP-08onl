from selenium.webdriver.common.by import By

contact_us_button = (By.ID, 'contact-link')
submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')

dresses = (By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a')
cart_button = (By.CLASS_NAME, 'shopping_cart')
sort_field = (By.CSS_SELECTOR, 'select[id="selectProductSort"]')
search_field = (By.CSS_SELECTOR, 'input[class="search_query form-control ac_input"]')
