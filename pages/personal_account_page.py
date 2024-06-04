from locators.login_page_locators import StellarBurgerRegistrationLocators as RL
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.personal_account_locators import StellarBurgerRestorePersonalAccountPage as PA
from pages.base_page import BasePage


class StellarBurgerPersonalAccountPage(BasePage):
    @allure.step("Клик на кнопку История заказов")
    def click_order_history_button(self):
        self.driver.find_element(*PA.ORDER_HISTORY_BUTTON).click()

    @allure.step("Заполнение поля Email")
    def wait_until_exit_button_show(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PA.EXIT_BUTTON))
    @allure.step("Клик на кнопку Выйти из аккаунта")
    def click_exit_button(self):
        self.driver.find_element(*PA.EXIT_BUTTON).click()

    @allure.step("Получение номера последнего заказа пользователя")
    def get_user_last_order_number(self):
        order = self.driver.find_element(*PA.USER_ORDERS_HISTORY).text
        return order
