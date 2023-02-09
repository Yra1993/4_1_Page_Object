from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time 

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    page.chek_product_inside_basket()
    #time.sleep(1000)