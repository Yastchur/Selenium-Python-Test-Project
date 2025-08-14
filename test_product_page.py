import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

@pytest.mark.login_on_product_page
class TestLoginOnProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, url)
        self.page.open()
    
    def test_guest_should_see_login_link_on_product_page(self):
        self.page.should_be_login_link()
    
    @pytest.mark.need_review   
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.page.go_to_login_page()    

@pytest.mark.success_message_on_product_page
class TestSuccessMessageOnProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        self.page = ProductPage(browser, url)
        self.page.open()
        
    @pytest.mark.xfail(reason="Сообщение появляется после добавления товара — ожидаемое поведение")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.page.add_product_to_basket()
        self.page.should_not_be_success_message()
        
    @pytest.mark.xfail(reason="Сообщение не исчезает автоматически — баг или фича")
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.page.add_product_to_basket()
        self.page.should_disappear_success_message()
        
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self):
        self.page.add_product_to_basket()
        self.page.should_be_correct_product_in_basket()
        self.page.should_be_correct_price_in_basket()

@pytest.mark.product_page
class TestSuccessMessageOnProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        self.page = ProductPage(browser, url)
        self.page.open()
        
    def test_guest_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        self.page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_empty_basket_text()
        
    

@pytest.mark.user_on_product_page
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, login_url)
        login_page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "securePassword123"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

        self.link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        self.page = ProductPage(browser, self.link)
        self.page.open()

    def test_user_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.page.add_product_to_basket()
        self.page.should_be_correct_product_in_basket()
        self.page.should_be_correct_price_in_basket()

