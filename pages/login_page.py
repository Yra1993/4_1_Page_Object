from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from pages.main_page import MainPage
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url=self.browser.current_url
        assert "login" in current_url, "Login url is not corect" # сообщение об ошибке

    def should_be_login_form(self):
        #MainPage.go_to_login_page()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        #MainPage.go_to_login_page()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"