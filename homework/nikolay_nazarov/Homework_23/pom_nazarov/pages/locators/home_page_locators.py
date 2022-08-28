from selenium.webdriver.common.by import By


sign_in_button = (By.CLASS_NAME, 'login')
go_to_login_screen_button = (By.CSS_SELECTOR,
                             'div[class="header__userzone-image header__userzone-image--auth"]')
confirm_address_button = (By.CSS_SELECTOR, '.b-location-confirmation__buttons-list button')
login_input = (By.CSS_SELECTOR, 'input[placeholder="Телефон или электронная почта"]')
password_input = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
submit_button = (By.CSS_SELECTOR, 'button[data-test-id="button-login"]')
buy_button = (By.CSS_SELECTOR, 'button[data-test-id="product-buy-btn"]')
item_name = (By.CSS_SELECTOR, '.product-card__title')
my_cart_button = (By.CSS_SELECTOR, '.header__userzone-control--basket')
