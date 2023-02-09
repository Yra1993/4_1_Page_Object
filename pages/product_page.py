from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        Basket = self.browser.find_element(*LoginPageLocators.BASKET_BUTTON)
        Basket.click()
        #self.solve_quiz_and_get_code()
    #def should_be_login_link(self):
     #   assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def chek_product_inside_basket(self):
        #MainPage.go_to_login_page()
        PRODUCT_BASKET_MESSAGE = self.browser.find_element(*LoginPageLocators.PRODUCT_INPUT_BASKET_MESSAGE)
        PRODUCT_BASKET_MESSAGE = PRODUCT_BASKET_MESSAGE.text
        PRODUCT_NAME=self.browser.find_element(*LoginPageLocators.PRODUCT_NAME)
        PRODUCT_NAME = PRODUCT_NAME.text
        assert PRODUCT_NAME in PRODUCT_BASKET_MESSAGE, "Login url is not corect"
        print(f"{PRODUCT_NAME} был добавлен в вашу корзину")
    def chek_product_price_inside_basket(self):
        #MainPage.go_to_login_page()
        PRODUCT_PRICE_INPUT_BASKET_MESSAGE = self.browser.find_element(*LoginPageLocators.PRODUCT_PRICE_INPUT_BASKET_MESSAGE)
        PRODUCT_PRICE_INPUT_BASKET_MESSAGE = PRODUCT_PRICE_INPUT_BASKET_MESSAGE.text
        PRODUCT_PRICE=self.browser.find_element(*LoginPageLocators.PRODUCT_PRICE)
        PRODUCT_PRICE = PRODUCT_PRICE.text
        assert PRODUCT_PRICE in PRODUCT_PRICE_INPUT_BASKET_MESSAGE, "Login url is not corect"
        print(f"Цена в корзине равна цене товара")
