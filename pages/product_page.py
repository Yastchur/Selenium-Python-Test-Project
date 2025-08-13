from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert product_name == basket_name, f"Expected product name '{product_name}', got '{basket_name}'"

    def should_be_correct_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, f"Expected price '{product_price}', got '{basket_price}'"
