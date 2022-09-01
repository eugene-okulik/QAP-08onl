from selenium.webdriver.common.by import By

mail = (By.ID, "email")
order = (By.ID, "id_order")
message = (By.ID, "message")
submit = (By.ID, "submitMessage")
alert_msg = (By.CSS_SELECTOR, "#center_column > div")
search = (By.ID, "search_query_top")
search_sub = (By.CSS_SELECTOR, '#searchbox > button')
search_res = (By.CLASS_NAME, "heading-counter")
cart = (By. CSS_SELECTOR, '#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a > b')
alert_cart = (By.CSS_SELECTOR, '#center_column > p')
