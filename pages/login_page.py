from locators.login_page_locators import StellarBurgerRegistrationLocators as RL
import allure
from pages.base_page import BasePage


class StellarBurgerLoginPage(BasePage):

    @allure.step("Клик на кнопку Восстановить пароль")
    def click_restore_button(self):
        self.driver.find_element(*RL.RESTORE_PASSWORD_BUTTON).click()

    @allure.step("Заполнение поля Email")
    def email_field_fill(self, email):
        self.driver.find_element(*RL.EMAIL_FIELD).send_keys(email)

    @allure.step("Заполнение поля Пароль")
    def password_field_fill(self, password):
        self.driver.find_element(*RL.PASSWORD_FIELD).send_keys(password)

    @allure.step("Клик на кнопку Логин")
    def click_login_button(self):
        self.driver.find_element(*RL.LOGIN_BUTTON).click()
