from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']")
    PRODUCT_INPUT_BASKET_MESSAGE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']")
    PRODUCT_NAME=(By.CSS_SELECTOR, ".product_main h1")