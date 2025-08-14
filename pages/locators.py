from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
