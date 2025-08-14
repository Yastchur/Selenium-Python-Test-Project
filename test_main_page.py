import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_login_link()      # выполняем проверку наличия переходим на страницу логина
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    def test_guest_see_login_anr_register_form_on_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_login_page()      # реализуйте проверку

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_text()
