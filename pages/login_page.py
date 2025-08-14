from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        errors = []

        try:
            self.should_be_login_url()
        except AssertionError as e:
            errors.append(str(e))

        try:
            self.should_be_login_form()
        except AssertionError as e:
            errors.append(str(e))

        try:
            self.should_be_register_form()
        except AssertionError as e:
            errors.append(str(e))

        if errors:
            raise AssertionError(f"Ошибки :{' '.join(errors)}")

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL не содержит 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"
        
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
