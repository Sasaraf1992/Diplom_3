from locators.login_page_locators import StellarBurgerRegistrationLocators as RL
import allure
from pages.base_page import BasePage


class StellarBurgerLoginPage(BasePage):

    @allure.step("Клик на кнопку Восстановить пароль")
    def click_restore_button(self):
        self.find_element_with_click(RL.RESTORE_PASSWORD_BUTTON)

    @allure.step("Заполнение поля Email")
    def email_field_fill(self, email):
        self.send_keys_element(RL.EMAIL_FIELD, email)

    @allure.step("Заполнение поля Пароль")
    def password_field_fill(self, password):
        self.send_keys_element(RL.PASSWORD_FIELD, password)

    @allure.step("Клик на кнопку Логин")
    def click_login_button(self):
        self.find_element_with_click(RL.LOGIN_BUTTON)
